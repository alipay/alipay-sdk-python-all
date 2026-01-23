#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerNameResponse(object):

    def __init__(self):
        self._customer_short_name = None
        self._ep_name = None

    @property
    def customer_short_name(self):
        return self._customer_short_name

    @customer_short_name.setter
    def customer_short_name(self, value):
        self._customer_short_name = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_short_name:
            if hasattr(self.customer_short_name, 'to_alipay_dict'):
                params['customer_short_name'] = self.customer_short_name.to_alipay_dict()
            else:
                params['customer_short_name'] = self.customer_short_name
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerNameResponse()
        if 'customer_short_name' in d:
            o.customer_short_name = d['customer_short_name']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        return o


