#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherPackageUseRule(object):

    def __init__(self):
        self._use_rule_desc = None

    @property
    def use_rule_desc(self):
        return self._use_rule_desc

    @use_rule_desc.setter
    def use_rule_desc(self, value):
        self._use_rule_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.use_rule_desc:
            if hasattr(self.use_rule_desc, 'to_alipay_dict'):
                params['use_rule_desc'] = self.use_rule_desc.to_alipay_dict()
            else:
                params['use_rule_desc'] = self.use_rule_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageUseRule()
        if 'use_rule_desc' in d:
            o.use_rule_desc = d['use_rule_desc']
        return o


