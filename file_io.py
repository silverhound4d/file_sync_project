import os
from pathlib import Path
from utils import Utils

import logger as log


class FileIO:
    def __init__(self, backup_folder: str, source_folder: str) -> None:
        self.backup_folder = Path(backup_folder)
        self.source_folder = Path(source_folder)

    @staticmethod
    def copy_file(source: Path, target: Path) -> None:
        """Copy a file and verify its integrity."""
        with open(source, "rb") as source_file:
            log.logger.debug(f"Read file from: {source}")
            with open(target, "wb+") as target_file:
                for part in source_file:
                    target_file.write(part)
                log.logger.debug(f"Copied file to: {target}")
                Utils.compare_hashed_files(Utils.hash_file(source_file), Utils.hash_file(target_file))

    @staticmethod
    def create_file_system_objects(backup_folder_path: Path, source_folder_path: Path) -> None:
        """Create file objects in the backup folder, if they don't exist."""
        for path_object in source_folder_path.rglob("*"):
            relative_path = Path(path_object.relative_to(source_folder_path))
            backup_abs_path = backup_folder_path / relative_path

            # Create directories.
            if path_object.is_dir() and not backup_abs_path.exists():
                os.mkdir(backup_abs_path)
                log.logger.info(f"Directory created: {backup_abs_path}")

            # Create files.
            if path_object.is_file() and not backup_abs_path.exists():
                FileIO.copy_file(path_object, backup_abs_path)
                log.logger.info(f"File successfully copied to: {backup_abs_path}")

    @staticmethod
    def delete_file_system_objects(backup_folder_path: Path, source_folder_path: Path) -> None:
        """Delete objects from the backup folder that no longer exist in the source folder."""
        bottom_up_file_tree = reversed(list(backup_folder_path.rglob("*")))  # os.walk(path, topdown=False)
        for path_object in bottom_up_file_tree:
            relative_path = Path(path_object.relative_to(backup_folder_path))
            backup_abs_path = backup_folder_path / relative_path
            source_abs_path = source_folder_path / relative_path

            # Remove files
            if path_object.is_file():
                if not source_abs_path.exists():
                    os.remove(backup_abs_path)
                    log.logger.info(f"File removed: {backup_abs_path}")

            # Remove directories
            if path_object.is_dir():
                if not source_abs_path.exists():
                    os.rmdir(backup_abs_path)
                    log.logger.info(f"Directory removed: {backup_abs_path}")

    def sync_folders(self) -> None:
        """Synchronize select folders."""
        log.logger.debug("==== Initializing folder synchronization ====")
        self.create_file_system_objects(self.backup_folder, self.source_folder)
        self.delete_file_system_objects(self.backup_folder, self.source_folder)
