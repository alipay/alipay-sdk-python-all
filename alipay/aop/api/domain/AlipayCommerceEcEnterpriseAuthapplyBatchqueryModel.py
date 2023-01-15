#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEnterpriseAuthapplyBatchqueryModel(object):

    def __init__(self):
        self._auth_apply_id = None
        self._enterprise_id = None

    @property
    def auth_apply_id(self):
        return self._auth_apply_id

    @auth_apply_id.setter
    def auth_apply_id(self, value):
        self._auth_apply_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_apply_id:
            if hasattr(self.auth_apply_id, 'to_alipay_dict'):
                params['auth_apply_id'] = self.auth_apply_id.to_alipay_dict()
            else:
                params['auth_apply_id'] = self.auth_apply_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseAuthapplyBatchqueryModel()
        if 'auth_apply_id' in d:
            o.auth_apply_id = d['auth_apply_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        return o


