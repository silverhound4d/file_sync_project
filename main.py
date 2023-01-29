import argparse
from pathlib import Path

import crontab_management as cron_mng
from file_io import FileIO

parser = argparse.ArgumentParser()
parser.add_argument("backup", type=Path, help="Enter path to the backup FOLDER.")
parser.add_argument("source", type=Path, help="Enter path to the source FOLDER.")
parser.add_argument("log_path", type=Path, help="Enter path to the log FILE.")
parser.add_argument("-i", "--interval", type=int, help="Specify, how often to synchronize the folders (in minutes).")
args = parser.parse_args()

if __name__ == '__main__':
    file_io = FileIO(args.backup, args.source)
    file_io.sync_folders()
    cron_mng.schedule_file_sync_cron_job(args)

