#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BoxOrderStatusInfo import BoxOrderStatusInfo


class BoxExclusiveBase(object):

    def __init__(self):
        self._base_order_info = None
        self._brand_name = None
        self._desc = None
        self._main_id = None
        self._main_type = None
        self._material_type = None
        self._material_url = None
        self._pid = None

    @property
    def base_order_info(self):
        return self._base_order_info

    @base_order_info.setter
    def base_order_info(self, value):
        if isinstance(value, BoxOrderStatusInfo):
            self._base_order_info = value
        else:
            self._base_order_info = BoxOrderStatusInfo.from_alipay_dict(value)
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def main_id(self):
        return self._main_id

    @main_id.setter
    def main_id(self, value):
        self._main_id = value
    @property
    def main_type(self):
        return self._main_type

    @main_type.setter
    def main_type(self, value):
        self._main_type = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_order_info:
            if hasattr(self.base_order_info, 'to_alipay_dict'):
                params['base_order_info'] = self.base_order_info.to_alipay_dict()
            else:
                params['base_order_info'] = self.base_order_info
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.main_id:
            if hasattr(self.main_id, 'to_alipay_dict'):
                params['main_id'] = self.main_id.to_alipay_dict()
            else:
                params['main_id'] = self.main_id
        if self.main_type:
            if hasattr(self.main_type, 'to_alipay_dict'):
                params['main_type'] = self.main_type.to_alipay_dict()
            else:
                params['main_type'] = self.main_type
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.material_url:
            if hasattr(self.material_url, 'to_alipay_dict'):
                params['material_url'] = self.material_url.to_alipay_dict()
            else:
                params['material_url'] = self.material_url
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxExclusiveBase()
        if 'base_order_info' in d:
            o.base_order_info = d['base_order_info']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'desc' in d:
            o.desc = d['desc']
        if 'main_id' in d:
            o.main_id = d['main_id']
        if 'main_type' in d:
            o.main_type = d['main_type']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'material_url' in d:
            o.material_url = d['material_url']
        if 'pid' in d:
            o.pid = d['pid']
        return o


