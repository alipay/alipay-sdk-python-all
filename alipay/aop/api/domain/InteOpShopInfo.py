#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpShopInfo(object):

    def __init__(self):
        self._shop_city_code = None
        self._shop_country_code = None
        self._shop_detail_address = None
        self._shop_district_code = None
        self._shop_name = None
        self._shop_province_code = None
        self._shop_scene_pic = None
        self._shop_sign_board_pic = None

    @property
    def shop_city_code(self):
        return self._shop_city_code

    @shop_city_code.setter
    def shop_city_code(self, value):
        self._shop_city_code = value
    @property
    def shop_country_code(self):
        return self._shop_country_code

    @shop_country_code.setter
    def shop_country_code(self, value):
        self._shop_country_code = value
    @property
    def shop_detail_address(self):
        return self._shop_detail_address

    @shop_detail_address.setter
    def shop_detail_address(self, value):
        self._shop_detail_address = value
    @property
    def shop_district_code(self):
        return self._shop_district_code

    @shop_district_code.setter
    def shop_district_code(self, value):
        self._shop_district_code = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_province_code(self):
        return self._shop_province_code

    @shop_province_code.setter
    def shop_province_code(self, value):
        self._shop_province_code = value
    @property
    def shop_scene_pic(self):
        return self._shop_scene_pic

    @shop_scene_pic.setter
    def shop_scene_pic(self, value):
        self._shop_scene_pic = value
    @property
    def shop_sign_board_pic(self):
        return self._shop_sign_board_pic

    @shop_sign_board_pic.setter
    def shop_sign_board_pic(self, value):
        self._shop_sign_board_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_city_code:
            if hasattr(self.shop_city_code, 'to_alipay_dict'):
                params['shop_city_code'] = self.shop_city_code.to_alipay_dict()
            else:
                params['shop_city_code'] = self.shop_city_code
        if self.shop_country_code:
            if hasattr(self.shop_country_code, 'to_alipay_dict'):
                params['shop_country_code'] = self.shop_country_code.to_alipay_dict()
            else:
                params['shop_country_code'] = self.shop_country_code
        if self.shop_detail_address:
            if hasattr(self.shop_detail_address, 'to_alipay_dict'):
                params['shop_detail_address'] = self.shop_detail_address.to_alipay_dict()
            else:
                params['shop_detail_address'] = self.shop_detail_address
        if self.shop_district_code:
            if hasattr(self.shop_district_code, 'to_alipay_dict'):
                params['shop_district_code'] = self.shop_district_code.to_alipay_dict()
            else:
                params['shop_district_code'] = self.shop_district_code
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_province_code:
            if hasattr(self.shop_province_code, 'to_alipay_dict'):
                params['shop_province_code'] = self.shop_province_code.to_alipay_dict()
            else:
                params['shop_province_code'] = self.shop_province_code
        if self.shop_scene_pic:
            if hasattr(self.shop_scene_pic, 'to_alipay_dict'):
                params['shop_scene_pic'] = self.shop_scene_pic.to_alipay_dict()
            else:
                params['shop_scene_pic'] = self.shop_scene_pic
        if self.shop_sign_board_pic:
            if hasattr(self.shop_sign_board_pic, 'to_alipay_dict'):
                params['shop_sign_board_pic'] = self.shop_sign_board_pic.to_alipay_dict()
            else:
                params['shop_sign_board_pic'] = self.shop_sign_board_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpShopInfo()
        if 'shop_city_code' in d:
            o.shop_city_code = d['shop_city_code']
        if 'shop_country_code' in d:
            o.shop_country_code = d['shop_country_code']
        if 'shop_detail_address' in d:
            o.shop_detail_address = d['shop_detail_address']
        if 'shop_district_code' in d:
            o.shop_district_code = d['shop_district_code']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_province_code' in d:
            o.shop_province_code = d['shop_province_code']
        if 'shop_scene_pic' in d:
            o.shop_scene_pic = d['shop_scene_pic']
        if 'shop_sign_board_pic' in d:
            o.shop_sign_board_pic = d['shop_sign_board_pic']
        return o


