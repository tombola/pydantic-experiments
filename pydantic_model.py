"""
https://docs.pydantic.dev/usage/models
"""

from datetime import datetime
from pydantic import BaseModel

from objexplore import explore
from rich import print

class Acquisition(BaseModel):
    crop: str
    crop_variety: str | None = None
    sku: str
    wc_product_id: int
    wc_product_variation_ids: list[int] = []
    stock: int = 0


external_data = {
    'crop': 'Onion',
    'crop_variety': 'Zebrune',
    'sku': 'OnZb',
    'wc_product_id': 123,
    'wc_product_variation_ids': [1234, '12345'],
}

acquisition = Acquisition(**external_data)

# explore(acquisition)
print(acquisition.crop)
# print(acquisition.json())
print(acquisition.dict())

# print(acquisition.crop_variety)
# print(acquisition.sku)
# print(acquisition.wc_product_id)
# print(acquisition.wc_product_variation_ids)

# Test aliases

# Test loading settings
# https://docs.pydantic.dev/usage/settings/