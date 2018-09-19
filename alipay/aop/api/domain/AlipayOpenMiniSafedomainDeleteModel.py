#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniSafedomainDeleteModel(object):

    def __init__(self):
        self._safe_domain = None

    @property
    def safe_domain(self):
        return self._safe_domain

    @safe_domain.setter
    def safe_domain(self, value):
        self._safe_domain = value


    def to_alipay_dict(self):
        params = dict()
        if self.safe_domain:
            if hasattr(self.safe_domain, 'to_alipay_dict'):
                params['safe_domain'] = self.safe_domain.to_alipay_dict()
            else:
                params['safe_domain'] = self.safe_domain
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniSafedomainDeleteModel()
        if 'safe_domain' in d:
            o.safe_domain = d['safe_domain']
        return o


