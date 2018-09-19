#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMerchant(object):

    def __init__(self):
        self._name = None
        self._service_phone = None
        self._short_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.short_name:
            if hasattr(self.short_name, 'to_alipay_dict'):
                params['short_name'] = self.short_name.to_alipay_dict()
            else:
                params['short_name'] = self.short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMerchant()
        if 'name' in d:
            o.name = d['name']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'short_name' in d:
            o.short_name = d['short_name']
        return o


