class GroupHelper {
    [string]$Server
    [string]$Username
    [string]$Password

    GroupHelper([string]$server, [string]$username, [string]$password) {
        $this.Server = $server
        $this.Username = $username
        $this.Password = $password
    }

    [System.Management.Automation.Runspaces.PSSession] CreateRemoteSession() {
        $securePassword = ConvertTo-SecureString $this.Password -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($this.Username, $securePassword)
        return New-PSSession -ComputerName $this.Server -Credential $credential
    }

    [PSObject] GetGroupByIdentity([string]$identity) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($identity)
            try {
                Get-ADGroup -Identity $identity
            } catch {
                return $null
            }
        } -ArgumentList $identity
        Remove-PSSession -Session $session
        return $result
    }

    [bool] CheckGroupExists([string]$identity) {
        $group = $this.GetGroupByIdentity($identity)
        return $null -ne $group
    }

    [array] GetGroupsByUser([string]$userIdentity) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($userIdentity)
            try {
                Get-ADUser -Identity $userIdentity | Get-ADPrincipalGroupMembership
            } catch {
                return @()
            }
        } -ArgumentList $userIdentity
        Remove-PSSession -Session $session
        return $result
    }

    [array] GetUsersByGroup([string]$groupName) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($groupName)
            try {
                Get-ADGroupMember -Identity $groupName | Where-Object { $_.objectClass -eq "user" }
            } catch {
                return @()
            }
        } -ArgumentList $groupName
        Remove-PSSession -Session $session
        return $result
    }

    AddNewGroup([string]$groupName, [string]$description, [string]$OU) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($groupName, $description, $OU)
            try {
                New-ADGroup -Name $groupName -GroupScope Global -GroupCategory Security -Description $description -Path $OU
            } catch {
                Write-Error "Error creating group: $_"
            }
        } -ArgumentList $groupName, $description, $OU
        Remove-PSSession -Session $session
    }

    AddGroupToGroup([string]$parentGroup, [string]$childGroup) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($parentGroup, $childGroup)
            try {
                Add-ADGroupMember -Identity $parentGroup -Members $childGroup
            } catch {
                Write-Error "Error adding group to group: $_"
            }
        } -ArgumentList $parentGroup, $childGroup
        Remove-PSSession -Session $session
    }

    MoveGroupToOU([string]$groupName, [string]$newOU) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($groupName, $newOU)
            try {
                Move-ADObject -Identity (Get-ADGroup -Identity $groupName).DistinguishedName -TargetPath $newOU
            } catch {
                Write-Error "Error moving group: $_"
            }
        } -ArgumentList $groupName, $newOU
        Remove-PSSession -Session $session
    }

    RemoveGroup([string]$groupName) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($groupName)
            try {
                Remove-ADGroup -Identity $groupName -Confirm:$false
            } catch {
                Write-Error "Error removing group: $_"
            }
        } -ArgumentList $groupName
        Remove-PSSession -Session $session
    }

    RemoveGroupFromGroup([string]$parentGroup, [string]$childGroup) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($parentGroup, $childGroup)
            try {
                Remove-ADGroupMember -Identity $parentGroup -Members $childGroup -Confirm:$false
            } catch {
                Write-Error "Error removing group from group: $_"
            }
        } -ArgumentList $parentGroup, $childGroup
        Remove-PSSession -Session $session
    }
}