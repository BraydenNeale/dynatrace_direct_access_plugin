import subprocess
import json
import logging
import tempfile
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name

class DirectAccessUserPlugin(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('oneagent_sdk.demo_app'))
        pgi_id = pgi.group_instance_id
        
        tempdir = tempfile.gettempdir()
        json_file_path = "{0}\\object.json".format(tempdir)
        powershell_command = "get-WmiObject win32_logicaldisk | Select-Object FreeSpace, Size, DriveType | ConvertTo-Json | Out-File {0} -Encoding UTF8".format(json_file_path)
        p1 = subprocess.Popen(["powershell", powershell_command]);
        p1.wait()

        stats = {}
        with open(json_file_path, encoding='utf-8') as json_file:
            clean_file = json_file.read()
            clean_file = clean_file.replace('\ufeff', '')
            stats = json.loads(clean_file)

        self.results_builder.absolute(key='free_space', value=stats['FreeSpace'], entity_id=pgi_id)
        self.results_builder.absolute(key='disk_size', value=stats['Size'], entity_id=pgi_id)
        self.results_builder.absolute(key='drive_type', value=stats['DriveType'], entity_id=pgi_id)
        '''
        self.results_builder.absolute(key='total_connections', value=stats['TotalConnections'], entity_id=pgi_id)
        self.results_builder.relative(key='total_DA_connections', value=stats['TotalDAConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_vpn_connections', value=stats['TotalVpnConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_unique_users', value=stats['TotalUniqueUsers'], entity_id=pgi_id)
        self.results_builder.absolute(key='max_concurrent_connections', value=stats['MaxConcurrentConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_cumulative_connections', value=stats['TotalCumulativeConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_bytes_in', value=stats['TotalBytesIn'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_bytes_out', value=stats['TotalBytesOut'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_bytes_in_out', value=stats['TotalBytesInOut'], entity_id=pgi_id)
        '''