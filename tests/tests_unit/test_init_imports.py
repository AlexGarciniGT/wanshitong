import wanshitong as wst

import unittest

class TestImportWST(unittest.TestCase):
    def test_import_wst(self):
        try:
            import wanshitong as wst
        except ImportError as e:
            self.fail(f"No se pudo importar wanshitong: {e}")

        self.assertIsNotNone(wst, "El módulo wst es None después de importarlo")
        
        
class TestImportGeneral(unittest.TestCase):
    def test_import_wst(self):
        try:
            import wanshitong.general 
        except ImportError as e:
            self.fail(f"No se pudo importar wanshitong.general: {e}")

        self.assertIsNotNone(wst, "El módulo wst.general es None después de importarlo")


if __name__ == "__main__":
    unittest.main()
