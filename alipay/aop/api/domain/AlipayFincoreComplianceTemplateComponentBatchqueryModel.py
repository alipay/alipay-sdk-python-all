#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateComponentBatchqueryModel(object):

    def __init__(self):
        self._template_codes = None
        self._template_lib_code = None

    @property
    def template_codes(self):
        return self._template_codes

    @template_codes.setter
    def template_codes(self, value):
        if isinstance(value, list):
            self._template_codes = list()
            for i in value:
                self._template_codes.append(i)
    @property
    def template_lib_code(self):
        return self._template_lib_code

    @template_lib_code.setter
    def template_lib_code(self, value):
        self._template_lib_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.template_codes:
            if isinstance(self.template_codes, list):
                for i in range(0, len(self.template_codes)):
                    element = self.template_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_codes[i] = element.to_alipay_dict()
            if hasattr(self.template_codes, 'to_alipay_dict'):
                params['template_codes'] = self.template_codes.to_alipay_dict()
            else:
                params['template_codes'] = self.template_codes
        if self.template_lib_code:
            if hasattr(self.template_lib_code, 'to_alipay_dict'):
                params['template_lib_code'] = self.template_lib_code.to_alipay_dict()
            else:
                params['template_lib_code'] = self.template_lib_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceTemplateComponentBatchqueryModel()
        if 'template_codes' in d:
            o.template_codes = d['template_codes']
        if 'template_lib_code' in d:
            o.template_lib_code = d['template_lib_code']
        return o


