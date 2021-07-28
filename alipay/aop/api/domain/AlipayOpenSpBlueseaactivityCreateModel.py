#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpBlueseaactivityCreateModel(object):

    def __init__(self):
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
        self._merchant_logon = None
        self._province_code = None
        self._shop_entrance_pic = None
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


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_lic:
            if hasattr(self.business_lic, 'to_alipay_dict'):
                params['business_lic'] = self.business_lic.to_alipay_dict()
            else:
                params['business_lic'] = self.business_lic
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.food_business_lic:
            if hasattr(self.food_business_lic, 'to_alipay_dict'):
                params['food_business_lic'] = self.food_business_lic.to_alipay_dict()
            else:
                params['food_business_lic'] = self.food_business_lic
        if self.food_circulate_lic:
            if hasattr(self.food_circulate_lic, 'to_alipay_dict'):
                params['food_circulate_lic'] = self.food_circulate_lic.to_alipay_dict()
            else:
                params['food_circulate_lic'] = self.food_circulate_lic
        if self.food_health_lic:
            if hasattr(self.food_health_lic, 'to_alipay_dict'):
                params['food_health_lic'] = self.food_health_lic.to_alipay_dict()
            else:
                params['food_health_lic'] = self.food_health_lic
        if self.food_production_lic:
            if hasattr(self.food_production_lic, 'to_alipay_dict'):
                params['food_production_lic'] = self.food_production_lic.to_alipay_dict()
            else:
                params['food_production_lic'] = self.food_production_lic
        if self.food_service_lic:
            if hasattr(self.food_service_lic, 'to_alipay_dict'):
                params['food_service_lic'] = self.food_service_lic.to_alipay_dict()
            else:
                params['food_service_lic'] = self.food_service_lic
        if self.indoor_pic:
            if hasattr(self.indoor_pic, 'to_alipay_dict'):
                params['indoor_pic'] = self.indoor_pic.to_alipay_dict()
            else:
                params['indoor_pic'] = self.indoor_pic
        if self.merchant_logon:
            if hasattr(self.merchant_logon, 'to_alipay_dict'):
                params['merchant_logon'] = self.merchant_logon.to_alipay_dict()
            else:
                params['merchant_logon'] = self.merchant_logon
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.shop_entrance_pic:
            if hasattr(self.shop_entrance_pic, 'to_alipay_dict'):
                params['shop_entrance_pic'] = self.shop_entrance_pic.to_alipay_dict()
            else:
                params['shop_entrance_pic'] = self.shop_entrance_pic
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.tobacco_lic:
            if hasattr(self.tobacco_lic, 'to_alipay_dict'):
                params['tobacco_lic'] = self.tobacco_lic.to_alipay_dict()
            else:
                params['tobacco_lic'] = self.tobacco_lic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpBlueseaactivityCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_lic' in d:
            o.business_lic = d['business_lic']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'food_business_lic' in d:
            o.food_business_lic = d['food_business_lic']
        if 'food_circulate_lic' in d:
            o.food_circulate_lic = d['food_circulate_lic']
        if 'food_health_lic' in d:
            o.food_health_lic = d['food_health_lic']
        if 'food_production_lic' in d:
            o.food_production_lic = d['food_production_lic']
        if 'food_service_lic' in d:
            o.food_service_lic = d['food_service_lic']
        if 'indoor_pic' in d:
            o.indoor_pic = d['indoor_pic']
        if 'merchant_logon' in d:
            o.merchant_logon = d['merchant_logon']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'shop_entrance_pic' in d:
            o.shop_entrance_pic = d['shop_entrance_pic']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'tobacco_lic' in d:
            o.tobacco_lic = d['tobacco_lic']
        return o


