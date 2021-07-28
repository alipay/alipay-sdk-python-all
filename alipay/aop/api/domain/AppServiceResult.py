#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppServiceResult(object):

    def __init__(self):
        self._carrier_url = None
        self._logo_url = None
        self._service_code = None
        self._service_name = None
        self._simple_desc = None

    @property
    def carrier_url(self):
        return self._carrier_url

    @carrier_url.setter
    def carrier_url(self, value):
        self._carrier_url = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def simple_desc(self):
        return self._simple_desc

    @simple_desc.setter
    def simple_desc(self, value):
        self._simple_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.carrier_url:
            if hasattr(self.carrier_url, 'to_alipay_dict'):
                params['carrier_url'] = self.carrier_url.to_alipay_dict()
            else:
                params['carrier_url'] = self.carrier_url
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.simple_desc:
            if hasattr(self.simple_desc, 'to_alipay_dict'):
                params['simple_desc'] = self.simple_desc.to_alipay_dict()
            else:
                params['simple_desc'] = self.simple_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppServiceResult()
        if 'carrier_url' in d:
            o.carrier_url = d['carrier_url']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'simple_desc' in d:
            o.simple_desc = d['simple_desc']
        return o


