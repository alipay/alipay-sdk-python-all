#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcReceiptidentitygroupDeleteModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._identity_group_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def identity_group_id(self):
        return self._identity_group_id

    @identity_group_id.setter
    def identity_group_id(self, value):
        self._identity_group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.identity_group_id:
            if hasattr(self.identity_group_id, 'to_alipay_dict'):
                params['identity_group_id'] = self.identity_group_id.to_alipay_dict()
            else:
                params['identity_group_id'] = self.identity_group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcReceiptidentitygroupDeleteModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'identity_group_id' in d:
            o.identity_group_id = d['identity_group_id']
        return o


