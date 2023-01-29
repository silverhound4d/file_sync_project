IMPORTANT: Runs on LINUX only (and possibly Mac)

1. Clone project to your `home` folder.
2. `cd` into the project folder to make it your current working directory.
3. Create a virtual environment .
4. Activate your virtual environment and install dependencies `pip install -r requirements.txt`.
5. Launch the script from the command line and enter required arguments:
   * Path to the backup folder.
   * Path to the source folder.
   * Path to the log file (this must be a specific file, i.e. `~/my_log.log`).
6. Enter optional arguments:
   * An interval to specify how often the folders will be synchronized.

Example usage:
`python main.py /home/$USER/backup_folder /home/$USER/source_folder /home/$USER/test.log -i 1`
