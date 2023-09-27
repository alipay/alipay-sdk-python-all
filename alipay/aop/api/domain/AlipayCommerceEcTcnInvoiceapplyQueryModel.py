#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcTcnInvoiceapplyQueryModel(object):

    def __init__(self):
        self._apply_id = None
        self._platform_apply_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def platform_apply_id(self):
        return self._platform_apply_id

    @platform_apply_id.setter
    def platform_apply_id(self, value):
        self._platform_apply_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.platform_apply_id:
            if hasattr(self.platform_apply_id, 'to_alipay_dict'):
                params['platform_apply_id'] = self.platform_apply_id.to_alipay_dict()
            else:
                params['platform_apply_id'] = self.platform_apply_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcTcnInvoiceapplyQueryModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'platform_apply_id' in d:
            o.platform_apply_id = d['platform_apply_id']
        return o


