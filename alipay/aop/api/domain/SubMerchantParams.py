#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubMerchantParams(object):

    def __init__(self):
        self._sub_merchant_id = None
        self._sub_merchant_name = None
        self._sub_merchant_service_description = None
        self._sub_merchant_service_name = None

    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def sub_merchant_name(self):
        return self._sub_merchant_name

    @sub_merchant_name.setter
    def sub_merchant_name(self, value):
        self._sub_merchant_name = value
    @property
    def sub_merchant_service_description(self):
        return self._sub_merchant_service_description

    @sub_merchant_service_description.setter
    def sub_merchant_service_description(self, value):
        self._sub_merchant_service_description = value
    @property
    def sub_merchant_service_name(self):
        return self._sub_merchant_service_name

    @sub_merchant_service_name.setter
    def sub_merchant_service_name(self, value):
        self._sub_merchant_service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.sub_merchant_name:
            if hasattr(self.sub_merchant_name, 'to_alipay_dict'):
                params['sub_merchant_name'] = self.sub_merchant_name.to_alipay_dict()
            else:
                params['sub_merchant_name'] = self.sub_merchant_name
        if self.sub_merchant_service_description:
            if hasattr(self.sub_merchant_service_description, 'to_alipay_dict'):
                params['sub_merchant_service_description'] = self.sub_merchant_service_description.to_alipay_dict()
            else:
                params['sub_merchant_service_description'] = self.sub_merchant_service_description
        if self.sub_merchant_service_name:
            if hasattr(self.sub_merchant_service_name, 'to_alipay_dict'):
                params['sub_merchant_service_name'] = self.sub_merchant_service_name.to_alipay_dict()
            else:
                params['sub_merchant_service_name'] = self.sub_merchant_service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubMerchantParams()
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'sub_merchant_name' in d:
            o.sub_merchant_name = d['sub_merchant_name']
        if 'sub_merchant_service_description' in d:
            o.sub_merchant_service_description = d['sub_merchant_service_description']
        if 'sub_merchant_service_name' in d:
            o.sub_merchant_service_name = d['sub_merchant_service_name']
        return o


