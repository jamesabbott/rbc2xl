# Powershell script for packaging on windows...

$PYINST = (get-command pyinstaller.exe).Path
if ($PYINST -eq $null) {
    Write-Host "pyinstaller.exe not found"
    exit 1
} else {
    [System.Console]::WriteLine("pyinstaller.exe found: $PYINST")
}

$paths = 'build', 'dist', 'rbc2xl.spec'
foreach ($path in $paths) {
    if (Test-Path -LiteralPath $path) {
      Remove-Item -LiteralPath $path -Verbose -Recurse
    } else {
      "Path doesn't exist: $path"
    }
}

&$PYINST ./rbc2xl.py -w --onefile