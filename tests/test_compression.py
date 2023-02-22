import unittest

import compression as tar


class TestCompression(unittest.TestCase):

    def setUp(self):
        pass

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
        assert True


if __name__ == "__main__":
    unittest.main()
