#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceProductInfo import DeviceProductInfo


class MobileAppInfo(object):

    def __init__(self):
        self._bind_mini_app_count = None
        self._mobile_app_id = None
        self._mobile_app_name = None
        self._mobile_app_sign = None
        self._related_product_list = None

    @property
    def bind_mini_app_count(self):
        return self._bind_mini_app_count

    @bind_mini_app_count.setter
    def bind_mini_app_count(self, value):
        self._bind_mini_app_count = value
    @property
    def mobile_app_id(self):
        return self._mobile_app_id

    @mobile_app_id.setter
    def mobile_app_id(self, value):
        self._mobile_app_id = value
    @property
    def mobile_app_name(self):
        return self._mobile_app_name

    @mobile_app_name.setter
    def mobile_app_name(self, value):
        self._mobile_app_name = value
    @property
    def mobile_app_sign(self):
        return self._mobile_app_sign

    @mobile_app_sign.setter
    def mobile_app_sign(self, value):
        self._mobile_app_sign = value
    @property
    def related_product_list(self):
        return self._related_product_list

    @related_product_list.setter
    def related_product_list(self, value):
        if isinstance(value, list):
            self._related_product_list = list()
            for i in value:
                if isinstance(i, DeviceProductInfo):
                    self._related_product_list.append(i)
                else:
                    self._related_product_list.append(DeviceProductInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.bind_mini_app_count:
            if hasattr(self.bind_mini_app_count, 'to_alipay_dict'):
                params['bind_mini_app_count'] = self.bind_mini_app_count.to_alipay_dict()
            else:
                params['bind_mini_app_count'] = self.bind_mini_app_count
        if self.mobile_app_id:
            if hasattr(self.mobile_app_id, 'to_alipay_dict'):
                params['mobile_app_id'] = self.mobile_app_id.to_alipay_dict()
            else:
                params['mobile_app_id'] = self.mobile_app_id
        if self.mobile_app_name:
            if hasattr(self.mobile_app_name, 'to_alipay_dict'):
                params['mobile_app_name'] = self.mobile_app_name.to_alipay_dict()
            else:
                params['mobile_app_name'] = self.mobile_app_name
        if self.mobile_app_sign:
            if hasattr(self.mobile_app_sign, 'to_alipay_dict'):
                params['mobile_app_sign'] = self.mobile_app_sign.to_alipay_dict()
            else:
                params['mobile_app_sign'] = self.mobile_app_sign
        if self.related_product_list:
            if isinstance(self.related_product_list, list):
                for i in range(0, len(self.related_product_list)):
                    element = self.related_product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_product_list[i] = element.to_alipay_dict()
            if hasattr(self.related_product_list, 'to_alipay_dict'):
                params['related_product_list'] = self.related_product_list.to_alipay_dict()
            else:
                params['related_product_list'] = self.related_product_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MobileAppInfo()
        if 'bind_mini_app_count' in d:
            o.bind_mini_app_count = d['bind_mini_app_count']
        if 'mobile_app_id' in d:
            o.mobile_app_id = d['mobile_app_id']
        if 'mobile_app_name' in d:
            o.mobile_app_name = d['mobile_app_name']
        if 'mobile_app_sign' in d:
            o.mobile_app_sign = d['mobile_app_sign']
        if 'related_product_list' in d:
            o.related_product_list = d['related_product_list']
        return o


