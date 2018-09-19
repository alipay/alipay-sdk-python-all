#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishMaterialInfo(object):

    def __init__(self):
        self._add_price = None
        self._create_user = None
        self._ext_info = None
        self._material_id = None
        self._material_img = None
        self._material_name = None
        self._material_type = None
        self._max_num = None
        self._merchant_id = None
        self._public_id = None
        self._update_user = None

    @property
    def add_price(self):
        return self._add_price

    @add_price.setter
    def add_price(self, value):
        self._add_price = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_img(self):
        return self._material_img

    @material_img.setter
    def material_img(self, value):
        self._material_img = value
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def max_num(self):
        return self._max_num

    @max_num.setter
    def max_num(self, value):
        self._max_num = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_price:
            if hasattr(self.add_price, 'to_alipay_dict'):
                params['add_price'] = self.add_price.to_alipay_dict()
            else:
                params['add_price'] = self.add_price
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_img:
            if hasattr(self.material_img, 'to_alipay_dict'):
                params['material_img'] = self.material_img.to_alipay_dict()
            else:
                params['material_img'] = self.material_img
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.max_num:
            if hasattr(self.max_num, 'to_alipay_dict'):
                params['max_num'] = self.max_num.to_alipay_dict()
            else:
                params['max_num'] = self.max_num
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishMaterialInfo()
        if 'add_price' in d:
            o.add_price = d['add_price']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_img' in d:
            o.material_img = d['material_img']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'max_num' in d:
            o.max_num = d['max_num']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


