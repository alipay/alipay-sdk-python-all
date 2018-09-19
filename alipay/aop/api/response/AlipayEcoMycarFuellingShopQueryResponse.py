#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Product import Product
from alipay.aop.api.domain.Sale import Sale


class AlipayEcoMycarFuellingShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarFuellingShopQueryResponse, self).__init__()
        self._address = None
        self._city_code = None
        self._district_code = None
        self._lat = None
        self._lon = None
        self._out_shop_id = None
        self._pay_url = None
        self._poi_id = None
        self._product = None
        self._province_code = None
        self._sale = None
        self._shop_id = None
        self._shop_name = None
        self._shop_status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, list):
            self._product = list()
            for i in value:
                if isinstance(i, Product):
                    self._product.append(i)
                else:
                    self._product.append(Product.from_alipay_dict(i))
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, value):
        if isinstance(value, list):
            self._sale = list()
            for i in value:
                if isinstance(i, Sale):
                    self._sale.append(i)
                else:
                    self._sale.append(Sale.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarFuellingShopQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'lat' in response:
            self.lat = response['lat']
        if 'lon' in response:
            self.lon = response['lon']
        if 'out_shop_id' in response:
            self.out_shop_id = response['out_shop_id']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
        if 'poi_id' in response:
            self.poi_id = response['poi_id']
        if 'product' in response:
            self.product = response['product']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'sale' in response:
            self.sale = response['sale']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'shop_status' in response:
            self.shop_status = response['shop_status']
