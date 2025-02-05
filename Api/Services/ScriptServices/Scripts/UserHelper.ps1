class UserHelper {
    [string]$Server
    [string]$Username
    [string]$Password

    UserHelper([string]$server, [string]$username, [string]$password) {
        $this.Server = $server
        $this.Username = $username
        $this.Password = $password
    }

    [System.Management.Automation.Runspaces.PSSession] CreateRemoteSession() {
        $securePassword = ConvertTo-SecureString $this.Password -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($this.Username, $securePassword)
        $session = New-PSSession -ComputerName $this.Server -Credential $credential
        return $session

    }

    [string] GetUserDetails([string]$identity) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($id)
            $user = Get-ADUser -Filter "SamAccountName -like '$id'" -ErrorAction SilentlyContinue |
                Select-Object DistinguishedName, Enabled, GivenName, Name, ObjectClass, ObjectGUID, SamAccountName, SID, Surname, UserPrincipalName |
                ConvertTo-Json -Depth 3
            return $user
            } -ArgumentList $identity
    
            Remove-PSSession $session
    
            if ($result) {
                return $result
            } else {
                return "{}"
            }
        }

    [bool] CheckUserExists([string]$identity) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($identity)
            try {
                Get-ADUser -Identity $identity -ErrorAction Stop
                return $true
            } catch {
                return $false
            }
        } -ArgumentList $identity
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
                return $null
            }
        } -ArgumentList $groupName
        Remove-PSSession -Session $session
        return $result
    }

    [array] GetUsersByOU([string]$OU) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($OU)
            try {
                Get-ADUser -Filter * -SearchBase $OU
            } catch {
                return $null
            }
        } -ArgumentList $OU
        Remove-PSSession -Session $session
        return $result
    }

    AddNewUser([string]$username, [string]$password, [string]$firstName, [string]$lastName, [string]$email, [string]$OU) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($username, $password, $firstName, $lastName, $email, $OU)
            try {
                $name = "$firstName $lastName"
                $securePassword = ConvertTo-SecureString $password -AsPlainText -Force
                New-ADUser -SamAccountName $username -UserPrincipalName "$username@domain.com" -Name $name -GivenName $firstName -Surname $lastName -EmailAddress $email -AccountPassword $securePassword -Enabled $true -Path $OU
            } catch {
                Write-Error "Error creating user: $_"
            }
        } -ArgumentList $username, $password, $firstName, $lastName, $email, $OU
        Remove-PSSession -Session $session
    }

    AddUserToGroup([string]$username, [string]$groupName) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($username, $groupName)
            try {
                Add-ADGroupMember -Identity $groupName -Members $username
            } catch {
                Write-Error "Error adding user to group: $_"
            }
        } -ArgumentList $username, $groupName
        Remove-PSSession -Session $session
    }

    ResetUserPassword([string]$username, [string]$newPassword) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($username, $newPassword)
            try {
                $securePassword = ConvertTo-SecureString $newPassword -AsPlainText -Force
                Set-ADAccountPassword -Identity $username -NewPassword $securePassword -Reset
            } catch {
                Write-Error "Error resetting password: $_"
            }
        } -ArgumentList $username, $newPassword
        Remove-PSSession -Session $session
    }

    RemoveUser([string]$username) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($username)
            try {
                Remove-ADUser -Identity $username -Confirm:$false
            } catch {
                Write-Error "Error removing user: $_"
            }
        } -ArgumentList $username
        Remove-PSSession -Session $session
    }

    EnableUser([string]$username) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($username)
            try {
                Enable-ADAccount -Identity $username
            } catch {
                Write-Error "Error enabling user: $_"
            }
        } -ArgumentList $username
        Remove-PSSession -Session $session
    }

    DisableUser([string]$username) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($username)
            try {
                Disable-ADAccount -Identity $username
            } catch {
                Write-Error "Error disabling user: $_"
            }
        } -ArgumentList $username
        Remove-PSSession -Session $session
    }
}