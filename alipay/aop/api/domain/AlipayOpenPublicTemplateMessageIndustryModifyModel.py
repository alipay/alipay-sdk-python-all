#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicTemplateMessageIndustryModifyModel(object):

    def __init__(self):
        self._primary_industry_code = None
        self._primary_industry_name = None
        self._secondary_industry_code = None
        self._secondary_industry_name = None

    @property
    def primary_industry_code(self):
        return self._primary_industry_code

    @primary_industry_code.setter
    def primary_industry_code(self, value):
        self._primary_industry_code = value
    @property
    def primary_industry_name(self):
        return self._primary_industry_name

    @primary_industry_name.setter
    def primary_industry_name(self, value):
        self._primary_industry_name = value
    @property
    def secondary_industry_code(self):
        return self._secondary_industry_code

    @secondary_industry_code.setter
    def secondary_industry_code(self, value):
        self._secondary_industry_code = value
    @property
    def secondary_industry_name(self):
        return self._secondary_industry_name

    @secondary_industry_name.setter
    def secondary_industry_name(self, value):
        self._secondary_industry_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.primary_industry_code:
            if hasattr(self.primary_industry_code, 'to_alipay_dict'):
                params['primary_industry_code'] = self.primary_industry_code.to_alipay_dict()
            else:
                params['primary_industry_code'] = self.primary_industry_code
        if self.primary_industry_name:
            if hasattr(self.primary_industry_name, 'to_alipay_dict'):
                params['primary_industry_name'] = self.primary_industry_name.to_alipay_dict()
            else:
                params['primary_industry_name'] = self.primary_industry_name
        if self.secondary_industry_code:
            if hasattr(self.secondary_industry_code, 'to_alipay_dict'):
                params['secondary_industry_code'] = self.secondary_industry_code.to_alipay_dict()
            else:
                params['secondary_industry_code'] = self.secondary_industry_code
        if self.secondary_industry_name:
            if hasattr(self.secondary_industry_name, 'to_alipay_dict'):
                params['secondary_industry_name'] = self.secondary_industry_name.to_alipay_dict()
            else:
                params['secondary_industry_name'] = self.secondary_industry_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicTemplateMessageIndustryModifyModel()
        if 'primary_industry_code' in d:
            o.primary_industry_code = d['primary_industry_code']
        if 'primary_industry_name' in d:
            o.primary_industry_name = d['primary_industry_name']
        if 'secondary_industry_code' in d:
            o.secondary_industry_code = d['secondary_industry_code']
        if 'secondary_industry_name' in d:
            o.secondary_industry_name = d['secondary_industry_name']
        return o


