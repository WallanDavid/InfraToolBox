# verificar-ping-em-massa.ps1
# Testa vários hosts e mostra quem tá online

$hosts = @("8.8.8.8", "1.1.1.1", "google.com")

foreach ($host in $hosts) {
    if (Test-Connection -ComputerName $host -Count 1 -Quiet) {
        Write-Host "$host está ONLINE" -ForegroundColor Green
    } else {
        Write-Host "$host está OFFLINE" -ForegroundColor Red
    }
}
