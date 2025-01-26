$folderPath = "C:\Users\[ Set the path here Example ]Admin\Desktop\NewFolder"
$currentPassword = "Set-the-Password-here"

function Hide-Folder {
    if (Test-Path $folderPath) {
        attrib +h +s +r $folderPath
        cacls $folderPath /e /p everyone:n > $null
        Write-Output "Folder is now hidden and permission restricted."
    } else {
        Write-Output "Folder does not exist."
    }
}

function Unhide-Folder {
    if (Test-Path $folderPath) {
        attrib -h -s -r $folderPath
        cacls $folderPath /e /p everyone:f > $null
        Write-Output "Folder is now unhidden and permission granted."
    } else {
        Write-Output "Folder does not exist."
    }
}

# Main Script
Write-Output "Checking password for folder access..."
$enteredPassword = Read-Host "Enter password"

if ($enteredPassword -eq $currentPassword) {
    Write-Output "Correct password entered. Attempting to unhide folder..."
    Unhide-Folder
} else {
    Write-Output "Wrong password entered. Hiding the folder and redirecting to Desktop..."
    Hide-Folder
    Start-Process explorer.exe -ArgumentList "$env:USERPROFILE\Desktop"
    exit
}
