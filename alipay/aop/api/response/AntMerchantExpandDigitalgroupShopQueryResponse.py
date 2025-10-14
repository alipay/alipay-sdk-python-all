#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandDigitalgroupShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandDigitalgroupShopQueryResponse, self).__init__()
        self._address = None
        self._business_time = None
        self._category_final = None
        self._category_one = None
        self._city = None
        self._contact_phone = None
        self._digital_poi_id = None
        self._district = None
        self._g_name = None
        self._g_shopid = None
        self._latitude = None
        self._longitude = None
        self._province = None
        self._shop_business_status = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def category_final(self):
        return self._category_final

    @category_final.setter
    def category_final(self, value):
        self._category_final = value
    @property
    def category_one(self):
        return self._category_one

    @category_one.setter
    def category_one(self, value):
        self._category_one = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def digital_poi_id(self):
        return self._digital_poi_id

    @digital_poi_id.setter
    def digital_poi_id(self, value):
        self._digital_poi_id = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def g_name(self):
        return self._g_name

    @g_name.setter
    def g_name(self, value):
        self._g_name = value
    @property
    def g_shopid(self):
        return self._g_shopid

    @g_shopid.setter
    def g_shopid(self, value):
        self._g_shopid = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def shop_business_status(self):
        return self._shop_business_status

    @shop_business_status.setter
    def shop_business_status(self, value):
        self._shop_business_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandDigitalgroupShopQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'business_time' in response:
            self.business_time = response['business_time']
        if 'category_final' in response:
            self.category_final = response['category_final']
        if 'category_one' in response:
            self.category_one = response['category_one']
        if 'city' in response:
            self.city = response['city']
        if 'contact_phone' in response:
            self.contact_phone = response['contact_phone']
        if 'digital_poi_id' in response:
            self.digital_poi_id = response['digital_poi_id']
        if 'district' in response:
            self.district = response['district']
        if 'g_name' in response:
            self.g_name = response['g_name']
        if 'g_shopid' in response:
            self.g_shopid = response['g_shopid']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'province' in response:
            self.province = response['province']
        if 'shop_business_status' in response:
            self.shop_business_status = response['shop_business_status']
        if 'status' in response:
            self.status = response['status']
