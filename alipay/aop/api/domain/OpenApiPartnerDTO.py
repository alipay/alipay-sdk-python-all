#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiPartnerDTO(object):

    def __init__(self):
        self._company_code = None
        self._company_name = None

    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiPartnerDTO()
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'company_name' in d:
            o.company_name = d['company_name']
        return o


