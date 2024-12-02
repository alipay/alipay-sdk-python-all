#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddServicesInfo(object):

    def __init__(self):
        self._service_name = None
        self._service_price = None

    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_price(self):
        return self._service_price

    @service_price.setter
    def service_price(self, value):
        self._service_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_price:
            if hasattr(self.service_price, 'to_alipay_dict'):
                params['service_price'] = self.service_price.to_alipay_dict()
            else:
                params['service_price'] = self.service_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AddServicesInfo()
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_price' in d:
            o.service_price = d['service_price']
        return o


