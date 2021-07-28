#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceBase(object):

    def __init__(self):
        self._service_carrier_url = None
        self._service_code = None
        self._service_logo = None
        self._service_name = None
        self._service_simple_desc = None
        self._service_spec_code = None

    @property
    def service_carrier_url(self):
        return self._service_carrier_url

    @service_carrier_url.setter
    def service_carrier_url(self, value):
        self._service_carrier_url = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_logo(self):
        return self._service_logo

    @service_logo.setter
    def service_logo(self, value):
        self._service_logo = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_simple_desc(self):
        return self._service_simple_desc

    @service_simple_desc.setter
    def service_simple_desc(self, value):
        self._service_simple_desc = value
    @property
    def service_spec_code(self):
        return self._service_spec_code

    @service_spec_code.setter
    def service_spec_code(self, value):
        self._service_spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_carrier_url:
            if hasattr(self.service_carrier_url, 'to_alipay_dict'):
                params['service_carrier_url'] = self.service_carrier_url.to_alipay_dict()
            else:
                params['service_carrier_url'] = self.service_carrier_url
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_logo:
            if hasattr(self.service_logo, 'to_alipay_dict'):
                params['service_logo'] = self.service_logo.to_alipay_dict()
            else:
                params['service_logo'] = self.service_logo
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_simple_desc:
            if hasattr(self.service_simple_desc, 'to_alipay_dict'):
                params['service_simple_desc'] = self.service_simple_desc.to_alipay_dict()
            else:
                params['service_simple_desc'] = self.service_simple_desc
        if self.service_spec_code:
            if hasattr(self.service_spec_code, 'to_alipay_dict'):
                params['service_spec_code'] = self.service_spec_code.to_alipay_dict()
            else:
                params['service_spec_code'] = self.service_spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceBase()
        if 'service_carrier_url' in d:
            o.service_carrier_url = d['service_carrier_url']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_logo' in d:
            o.service_logo = d['service_logo']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_simple_desc' in d:
            o.service_simple_desc = d['service_simple_desc']
        if 'service_spec_code' in d:
            o.service_spec_code = d['service_spec_code']
        return o


