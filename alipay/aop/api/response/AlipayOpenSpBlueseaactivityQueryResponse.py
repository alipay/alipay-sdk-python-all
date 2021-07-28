#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpBlueseaactivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpBlueseaactivityQueryResponse, self).__init__()
        self._address = None
        self._biz_scene = None
        self._business_lic = None
        self._city_code = None
        self._district_code = None
        self._food_business_lic = None
        self._food_circulate_lic = None
        self._food_health_lic = None
        self._food_production_lic = None
        self._food_service_lic = None
        self._indoor_pic = None
        self._memo = None
        self._merchant_logon = None
        self._province_code = None
        self._shop_entrance_pic = None
        self._status = None
        self._sub_merchant_id = None
        self._tobacco_lic = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_lic(self):
        return self._business_lic

    @business_lic.setter
    def business_lic(self, value):
        self._business_lic = value
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
    def food_business_lic(self):
        return self._food_business_lic

    @food_business_lic.setter
    def food_business_lic(self, value):
        self._food_business_lic = value
    @property
    def food_circulate_lic(self):
        return self._food_circulate_lic

    @food_circulate_lic.setter
    def food_circulate_lic(self, value):
        self._food_circulate_lic = value
    @property
    def food_health_lic(self):
        return self._food_health_lic

    @food_health_lic.setter
    def food_health_lic(self, value):
        self._food_health_lic = value
    @property
    def food_production_lic(self):
        return self._food_production_lic

    @food_production_lic.setter
    def food_production_lic(self, value):
        self._food_production_lic = value
    @property
    def food_service_lic(self):
        return self._food_service_lic

    @food_service_lic.setter
    def food_service_lic(self, value):
        self._food_service_lic = value
    @property
    def indoor_pic(self):
        return self._indoor_pic

    @indoor_pic.setter
    def indoor_pic(self, value):
        self._indoor_pic = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_logon(self):
        return self._merchant_logon

    @merchant_logon.setter
    def merchant_logon(self, value):
        self._merchant_logon = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def shop_entrance_pic(self):
        return self._shop_entrance_pic

    @shop_entrance_pic.setter
    def shop_entrance_pic(self, value):
        self._shop_entrance_pic = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def tobacco_lic(self):
        return self._tobacco_lic

    @tobacco_lic.setter
    def tobacco_lic(self, value):
        self._tobacco_lic = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpBlueseaactivityQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'business_lic' in response:
            self.business_lic = response['business_lic']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'food_business_lic' in response:
            self.food_business_lic = response['food_business_lic']
        if 'food_circulate_lic' in response:
            self.food_circulate_lic = response['food_circulate_lic']
        if 'food_health_lic' in response:
            self.food_health_lic = response['food_health_lic']
        if 'food_production_lic' in response:
            self.food_production_lic = response['food_production_lic']
        if 'food_service_lic' in response:
            self.food_service_lic = response['food_service_lic']
        if 'indoor_pic' in response:
            self.indoor_pic = response['indoor_pic']
        if 'memo' in response:
            self.memo = response['memo']
        if 'merchant_logon' in response:
            self.merchant_logon = response['merchant_logon']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'shop_entrance_pic' in response:
            self.shop_entrance_pic = response['shop_entrance_pic']
        if 'status' in response:
            self.status = response['status']
        if 'sub_merchant_id' in response:
            self.sub_merchant_id = response['sub_merchant_id']
        if 'tobacco_lic' in response:
            self.tobacco_lic = response['tobacco_lic']
