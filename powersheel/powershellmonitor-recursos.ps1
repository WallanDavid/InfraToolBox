# monitor-recursos.ps1
# Script para monitorar uso de CPU e memória

Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 | Format-Table -AutoSize

$cpu = Get-WmiObject win32_processor | Measure-Object -Property LoadPercentage -Average | Select-Object Average
$mem = Get-WmiObject Win32_OperatingSystem

Write-Host "Uso da CPU: $($cpu.Average)%"
Write-Host "Memória livre: $([math]::Round($mem.FreePhysicalMemory / 1MB, 2)) MB"
