import hashlib
import logger as log

class Utils:
    @staticmethod
    def hash_file(opened_file) -> str:
        """Return hash of an already OPENED file."""
        sha256 = hashlib.sha256()
        content = opened_file.read()
        sha256.update(content)
        return sha256.hexdigest()

    @staticmethod
    def compare_hashed_files(file1: str, file2: str) -> None:
        """Compare hashes of two files."""
        try:
            assert file1 == file2
        except Exception as e:
            log.logger.error("Copied files are not identical!")
            log.logger.exception()

