from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Test Bun', 1234)
        assert bun.get_name() == 'Test Bun'

    def test_bun_get_price(self):
        bun = Bun('Test Bun', 1234)
        assert bun.get_price() == 1234
        