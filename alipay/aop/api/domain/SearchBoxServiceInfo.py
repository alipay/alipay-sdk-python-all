#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBoxServiceInfo(object):

    def __init__(self):
        self._service_category_code = None
        self._service_category_name = None
        self._service_code = None
        self._service_name = None

    @property
    def service_category_code(self):
        return self._service_category_code

    @service_category_code.setter
    def service_category_code(self, value):
        self._service_category_code = value
    @property
    def service_category_name(self):
        return self._service_category_name

    @service_category_name.setter
    def service_category_name(self, value):
        self._service_category_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.service_category_code:
            if hasattr(self.service_category_code, 'to_alipay_dict'):
                params['service_category_code'] = self.service_category_code.to_alipay_dict()
            else:
                params['service_category_code'] = self.service_category_code
        if self.service_category_name:
            if hasattr(self.service_category_name, 'to_alipay_dict'):
                params['service_category_name'] = self.service_category_name.to_alipay_dict()
            else:
                params['service_category_name'] = self.service_category_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxServiceInfo()
        if 'service_category_code' in d:
            o.service_category_code = d['service_category_code']
        if 'service_category_name' in d:
            o.service_category_name = d['service_category_name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        return o


