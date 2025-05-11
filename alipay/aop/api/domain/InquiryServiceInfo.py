#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InquiryServiceInfo(object):

    def __init__(self):
        self._platform_code = None
        self._pre_unit = None
        self._price = None
        self._service_mode = None
        self._service_name = None
        self._service_type = None
        self._service_url = None

    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def pre_unit(self):
        return self._pre_unit

    @pre_unit.setter
    def pre_unit(self, value):
        self._pre_unit = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def service_mode(self):
        return self._service_mode

    @service_mode.setter
    def service_mode(self, value):
        self._service_mode = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.pre_unit:
            if hasattr(self.pre_unit, 'to_alipay_dict'):
                params['pre_unit'] = self.pre_unit.to_alipay_dict()
            else:
                params['pre_unit'] = self.pre_unit
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.service_mode:
            if hasattr(self.service_mode, 'to_alipay_dict'):
                params['service_mode'] = self.service_mode.to_alipay_dict()
            else:
                params['service_mode'] = self.service_mode
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryServiceInfo()
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'pre_unit' in d:
            o.pre_unit = d['pre_unit']
        if 'price' in d:
            o.price = d['price']
        if 'service_mode' in d:
            o.service_mode = d['service_mode']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


