#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportUservoucherQueryModel(object):

    def __init__(self):
        self._arr_city = None
        self._arr_city_code = None
        self._dep_city = None
        self._dep_city_code = None
        self._ext_info = None
        self._open_id = None
        self._product_code = None
        self._scene_code = None
        self._user_id = None

    @property
    def arr_city(self):
        return self._arr_city

    @arr_city.setter
    def arr_city(self, value):
        self._arr_city = value
    @property
    def arr_city_code(self):
        return self._arr_city_code

    @arr_city_code.setter
    def arr_city_code(self, value):
        self._arr_city_code = value
    @property
    def dep_city(self):
        return self._dep_city

    @dep_city.setter
    def dep_city(self, value):
        self._dep_city = value
    @property
    def dep_city_code(self):
        return self._dep_city_code

    @dep_city_code.setter
    def dep_city_code(self, value):
        self._dep_city_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.arr_city:
            if hasattr(self.arr_city, 'to_alipay_dict'):
                params['arr_city'] = self.arr_city.to_alipay_dict()
            else:
                params['arr_city'] = self.arr_city
        if self.arr_city_code:
            if hasattr(self.arr_city_code, 'to_alipay_dict'):
                params['arr_city_code'] = self.arr_city_code.to_alipay_dict()
            else:
                params['arr_city_code'] = self.arr_city_code
        if self.dep_city:
            if hasattr(self.dep_city, 'to_alipay_dict'):
                params['dep_city'] = self.dep_city.to_alipay_dict()
            else:
                params['dep_city'] = self.dep_city
        if self.dep_city_code:
            if hasattr(self.dep_city_code, 'to_alipay_dict'):
                params['dep_city_code'] = self.dep_city_code.to_alipay_dict()
            else:
                params['dep_city_code'] = self.dep_city_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportUservoucherQueryModel()
        if 'arr_city' in d:
            o.arr_city = d['arr_city']
        if 'arr_city_code' in d:
            o.arr_city_code = d['arr_city_code']
        if 'dep_city' in d:
            o.dep_city = d['dep_city']
        if 'dep_city_code' in d:
            o.dep_city_code = d['dep_city_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


