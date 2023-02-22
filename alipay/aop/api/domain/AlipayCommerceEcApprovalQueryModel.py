#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcApprovalQueryModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._platform_approval_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def platform_approval_id(self):
        return self._platform_approval_id

    @platform_approval_id.setter
    def platform_approval_id(self, value):
        self._platform_approval_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.platform_approval_id:
            if hasattr(self.platform_approval_id, 'to_alipay_dict'):
                params['platform_approval_id'] = self.platform_approval_id.to_alipay_dict()
            else:
                params['platform_approval_id'] = self.platform_approval_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcApprovalQueryModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'platform_approval_id' in d:
            o.platform_approval_id = d['platform_approval_id']
        return o


