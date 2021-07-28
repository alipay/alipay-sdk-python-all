#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceCodeIstd import ServiceCodeIstd


class LogisticsCompanyIstd(object):

    def __init__(self):
        self._logistics_code = None
        self._service_codes = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def service_codes(self):
        return self._service_codes

    @service_codes.setter
    def service_codes(self, value):
        if isinstance(value, list):
            self._service_codes = list()
            for i in value:
                if isinstance(i, ServiceCodeIstd):
                    self._service_codes.append(i)
                else:
                    self._service_codes.append(ServiceCodeIstd.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.service_codes:
            if isinstance(self.service_codes, list):
                for i in range(0, len(self.service_codes)):
                    element = self.service_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_codes[i] = element.to_alipay_dict()
            if hasattr(self.service_codes, 'to_alipay_dict'):
                params['service_codes'] = self.service_codes.to_alipay_dict()
            else:
                params['service_codes'] = self.service_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsCompanyIstd()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'service_codes' in d:
            o.service_codes = d['service_codes']
        return o


