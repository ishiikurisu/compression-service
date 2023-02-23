import unittest

import compression as tar


class TestCompression(unittest.TestCase):

    def test_extract(self):
        binary = None
        with open("./tests/compressed_file.tar.gz", "rb") as fp:
            binary = fp.read()
        assert binary is not None

        temp_directory = "/tmp"
        files_before_extraction = tar.list_directory(temp_directory)
        extracted_files = tar.extract(binary)
        files_after_extraction = tar.list_directory(temp_directory)
        assert extracted_files is not None
        assert len(extracted_files) == 2
        assert files_after_extraction == files_before_extraction

    def test_compress(self):
        files = {
            "count.txt": "101",
            "friends.txt": "Finn, Jake, BMO\n",
        }
        temp_directory = "/tmp"
        files_before_compression = tar.list_directory(temp_directory)
        compressed_bytes = tar.compress(files)
        files_after_compression = tar.list_directory(temp_directory)
        assert compressed_bytes is not None
        assert files_after_compression == files_before_compression
        
        extracted_files = tar.extract(compressed_bytes)
        assert files == extracted_files

    def test_fail_to_decmopress_list(self):
        files = [
            "failure",
        ]
        temp_directory = "/tmp"
        files_before_compression = tar.list_directory(temp_directory)
        should_not_be_compressed_bytes = tar.compress(files)
        files_after_compression = tar.list_directory(temp_directory)
        assert should_not_be_compressed_bytes is None
        assert files_before_compression == files_after_compression


if __name__ == "__main__":
    unittest.main()
