class ComputerHelper {
    [string]$Server
    [string]$Username
    [string]$Password

    ComputerHelper([string]$server, [string]$username, [string]$password) {
        $this.Server = $server
        $this.Username = $username
        $this.Password = $password
    }

    [System.Management.Automation.Runspaces.PSSession] CreateRemoteSession() {
        $securePassword = ConvertTo-SecureString $this.Password -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($this.Username, $securePassword)
        return New-PSSession -ComputerName $this.Server -Credential $credential
    }

    [PSObject] GetComputerByName([string]$computerName) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($computerName)
            try {
                Get-ADComputer -Identity $computerName
            } catch {
                return $null
            }
        } -ArgumentList $computerName
        Remove-PSSession -Session $session
        return $result
    }

    [bool] CheckComputerExists([string]$computerName) {
        $computer = $this.GetComputerByName($computerName)
        return $null -ne $computer
    }

    [array] ListComputersInOU([string]$ouPath) {
        $session = $this.CreateRemoteSession()
        $result = Invoke-Command -Session $session -ScriptBlock {
            param($ouPath)
            try {
                Get-ADComputer -Filter * -SearchBase $ouPath | Select-Object Name, DistinguishedName
            } catch {
                return @()
            }
        } -ArgumentList $ouPath
        Remove-PSSession -Session $session
        return $result
    }

    AddNewComputer([string]$computerName, [string]$ouPath) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($computerName, $ouPath)
            try {
                New-ADComputer -Name $computerName -Path $ouPath
            } catch {
                Write-Error "Error creating computer account: $_"
            }
        } -ArgumentList $computerName, $ouPath
        Remove-PSSession -Session $session
    }

    MoveComputer([string]$computerName, [string]$newOU) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($computerName, $newOU)
            try {
                Move-ADObject -Identity (Get-ADComputer -Identity $computerName).DistinguishedName -TargetPath $newOU
            } catch {
                Write-Error "Error moving computer: $_"
            }
        } -ArgumentList $computerName, $newOU
        Remove-PSSession -Session $session
    }

    RemoveComputer([string]$computerName) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($computerName)
            try {
                Remove-ADComputer -Identity $computerName -Confirm:$false
            } catch {
                Write-Error "Error removing computer: $_"
            }
        } -ArgumentList $computerName
        Remove-PSSession -Session $session
    }

    ResetComputerAccount([string]$computerName) {
        $session = $this.CreateRemoteSession()
        Invoke-Command -Session $session -ScriptBlock {
            param($computerName)
            try {
                Reset-ADComputerAccountPassword -Identity $computerName
            } catch {
                Write-Error "Error resetting computer account: $_"
            }
        } -ArgumentList $computerName
        Remove-PSSession -Session $session
    }
}