import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", ["Краторная булка N-200i", "Флюоресцентная булка R2-D3"])
    def test_get_name(self, name):
        bun = Bun(name, 1255)
        
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", ["1255", "988"])
    def test_get_price(self, price):
        bun = Bun("Краторная булка N-200i", price)
            
        assert bun.get_price() == price