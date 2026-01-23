#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalCustomerQueryModel(object):

    def __init__(self):
        self._customer_name = None
        self._customer_short_name = None

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def customer_short_name(self):
        return self._customer_short_name

    @customer_short_name.setter
    def customer_short_name(self, value):
        self._customer_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.customer_short_name:
            if hasattr(self.customer_short_name, 'to_alipay_dict'):
                params['customer_short_name'] = self.customer_short_name.to_alipay_dict()
            else:
                params['customer_short_name'] = self.customer_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCustomerQueryModel()
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'customer_short_name' in d:
            o.customer_short_name = d['customer_short_name']
        return o


