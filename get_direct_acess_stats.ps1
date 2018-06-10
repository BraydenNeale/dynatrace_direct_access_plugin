# Run as a sheduled task every one minute
$StatPathJSON = 'D:\Software\Scripts\DirectAccessStats.JSON'
Get-RemoteAccessConnectionStatisticsSummary | Select-Object TotalConnections, TotalDAConnections, TotalVpnConnections, TotalUniqueUsers, MaxConcurrentConnections, TotalCumulativeConnections, TotalBytesIn, TotalBytesOut, TotalBytesInOut  | ConvertTo-Json | Out-File $StatPathJSON -Encoding UTF8