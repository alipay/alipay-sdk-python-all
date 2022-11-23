#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitUsageScopeDTO(object):

    def __init__(self):
        self._description = None
        self._usage_scope_type = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def usage_scope_type(self):
        return self._usage_scope_type

    @usage_scope_type.setter
    def usage_scope_type(self, value):
        self._usage_scope_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.usage_scope_type:
            if hasattr(self.usage_scope_type, 'to_alipay_dict'):
                params['usage_scope_type'] = self.usage_scope_type.to_alipay_dict()
            else:
                params['usage_scope_type'] = self.usage_scope_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitUsageScopeDTO()
        if 'description' in d:
            o.description = d['description']
        if 'usage_scope_type' in d:
            o.usage_scope_type = d['usage_scope_type']
        return o


