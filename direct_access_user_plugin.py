import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name
from ruxit.api.exceptions import ConfigException

class DirectAccessUserPlugin(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('DirectAccess'))
        pgi_id = pgi.group_instance_id

        json_file_path = "D:\\Software\\Scripts\\DirectAccessStats.JSON"
        stats = {}
        
        try:
            with open(json_file_path, encoding='utf-8') as json_file:
                clean_file = json_file.read().replace('\ufeff', '')
                try:
                    stats = json.loads(clean_file)
                except ValueError as ex:
                    raise ConfigException('Unable to parse "%s" as JSON' % json_file_path) from ex
        except IOError as ex:
            raise ConfigException('Could not open file "%s"' % json_file_path) from ex
        
        self.results_builder.absolute(key='total_connections', value=stats['TotalConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_DA_connections', value=stats['TotalDAConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_vpn_connections', value=stats['TotalVpnConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_unique_users', value=stats['TotalUniqueUsers'], entity_id=pgi_id)
        self.results_builder.absolute(key='max_concurrent_connections', value=stats['MaxConcurrentConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_cumulative_connections', value=stats['TotalCumulativeConnections'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_bytes_in', value=stats['TotalBytesIn'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_bytes_out', value=stats['TotalBytesOut'], entity_id=pgi_id)
        self.results_builder.absolute(key='total_bytes_in_out', value=stats['TotalBytesInOut'], entity_id=pgi_id)