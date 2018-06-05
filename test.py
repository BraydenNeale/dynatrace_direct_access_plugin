import subprocess
import json
import logging
import tempfile

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
    print(stats['Size'])