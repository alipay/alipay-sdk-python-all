#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateUseRuleInfo(object):

    def __init__(self):
        self._use_limit = None
        self._use_num_limit = None

    @property
    def use_limit(self):
        return self._use_limit

    @use_limit.setter
    def use_limit(self, value):
        self._use_limit = value
    @property
    def use_num_limit(self):
        return self._use_num_limit

    @use_num_limit.setter
    def use_num_limit(self, value):
        self._use_num_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.use_limit:
            if hasattr(self.use_limit, 'to_alipay_dict'):
                params['use_limit'] = self.use_limit.to_alipay_dict()
            else:
                params['use_limit'] = self.use_limit
        if self.use_num_limit:
            if hasattr(self.use_num_limit, 'to_alipay_dict'):
                params['use_num_limit'] = self.use_num_limit.to_alipay_dict()
            else:
                params['use_num_limit'] = self.use_num_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateUseRuleInfo()
        if 'use_limit' in d:
            o.use_limit = d['use_limit']
        if 'use_num_limit' in d:
            o.use_num_limit = d['use_num_limit']
        return o


