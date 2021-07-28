#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceProductInfo import DeviceProductInfo


class InvokeAppInfo(object):

    def __init__(self):
        self._invoke_app_id = None
        self._invoke_app_logo = None
        self._invoke_app_name = None
        self._related_product_list = None

    @property
    def invoke_app_id(self):
        return self._invoke_app_id

    @invoke_app_id.setter
    def invoke_app_id(self, value):
        self._invoke_app_id = value
    @property
    def invoke_app_logo(self):
        return self._invoke_app_logo

    @invoke_app_logo.setter
    def invoke_app_logo(self, value):
        self._invoke_app_logo = value
    @property
    def invoke_app_name(self):
        return self._invoke_app_name

    @invoke_app_name.setter
    def invoke_app_name(self, value):
        self._invoke_app_name = value
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
        if self.invoke_app_id:
            if hasattr(self.invoke_app_id, 'to_alipay_dict'):
                params['invoke_app_id'] = self.invoke_app_id.to_alipay_dict()
            else:
                params['invoke_app_id'] = self.invoke_app_id
        if self.invoke_app_logo:
            if hasattr(self.invoke_app_logo, 'to_alipay_dict'):
                params['invoke_app_logo'] = self.invoke_app_logo.to_alipay_dict()
            else:
                params['invoke_app_logo'] = self.invoke_app_logo
        if self.invoke_app_name:
            if hasattr(self.invoke_app_name, 'to_alipay_dict'):
                params['invoke_app_name'] = self.invoke_app_name.to_alipay_dict()
            else:
                params['invoke_app_name'] = self.invoke_app_name
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
        o = InvokeAppInfo()
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        if 'invoke_app_logo' in d:
            o.invoke_app_logo = d['invoke_app_logo']
        if 'invoke_app_name' in d:
            o.invoke_app_name = d['invoke_app_name']
        if 'related_product_list' in d:
            o.related_product_list = d['related_product_list']
        return o


