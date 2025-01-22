class OUHelper {
    [string]$Server
    [string]$Username
    [string]$Password

    OUHelper([string]$server, [string]$username, [string]$password) {
        $this.Server = $server
        $this.Username = $username
        $this.Password = $password
    }

    [System.Management.Automation.Runspaces.PSSession] CreateRemoteSession() {
        $securePassword = ConvertTo-SecureString $this.Password -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($this.Username, $securePassword)
        return New-PSSession -ComputerName $this.Server -Credential $credential
    }

    [PSObject] GetOUByIdentity([string]$identity) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($identity)
            try {
                Get-ADOrganizationalUnit -Identity $identity
            } catch {
                return $null
            }
        } -ArgumentList $identity
        Remove-PSSession -Session $session
        return $result
    }

    [bool] CheckOUExists([string]$identity) {
        $ou = $this.GetOUByIdentity($identity)
        return $null -ne $ou
    }

    [array] GetOUHierarch() {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            try {
                Get-ADOrganizationalUnit -Filter * | Select-Object DistinguishedName
            } catch {
                return @()
            }
        }
        Remove-PSSession -Session $session
        return $result
    }

    [array] ListOUs([string]$parentOU) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($parentOU)
            try {
                Get-ADOrganizationalUnit -Filter * -SearchBase $parentOU | Select-Object DistinguishedName
            } catch {
                return @()
            }
        } -ArgumentList $parentOU
        Remove-PSSession -Session $session
        return $result
    }

    AddNewOU([string]$ouName, [string]$parentOU) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($ouName, $parentOU)
            try {
                New-ADOrganizationalUnit -Name $ouName -Path $parentOU
            } catch {
                Write-Error "Error creating OU: $_"
            }
        } -ArgumentList $ouName, $parentOU
        Remove-PSSession -Session $session
    }

    MoveOU([string]$ouIdentity, [string]$newParentOU) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($ouIdentity, $newParentOU)
            try {
                Move-ADObject -Identity (Get-ADOrganizationalUnit -Identity $ouIdentity).DistinguishedName -TargetPath $newParentOU
            } catch {
                Write-Error "Error moving OU: $_"
            }
        } -ArgumentList $ouIdentity, $newParentOU
        Remove-PSSession -Session $session
    }

    RemoveOU([string]$ouIdentity) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($ouIdentity)
            try {
                Remove-ADOrganizationalUnit -Identity $ouIdentity -Recursive -Confirm:$false
            } catch {
                Write-Error "Error removing OU: $_"
            }
        } -ArgumentList $ouIdentity
        Remove-PSSession -Session $session
    }
}