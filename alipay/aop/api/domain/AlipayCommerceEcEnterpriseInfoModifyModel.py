#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEnterpriseInfoModifyModel(object):

    def __init__(self):
        self._enterprise_alias = None
        self._enterprise_id = None
        self._enterprise_name = None

    @property
    def enterprise_alias(self):
        return self._enterprise_alias

    @enterprise_alias.setter
    def enterprise_alias(self, value):
        self._enterprise_alias = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_alias:
            if hasattr(self.enterprise_alias, 'to_alipay_dict'):
                params['enterprise_alias'] = self.enterprise_alias.to_alipay_dict()
            else:
                params['enterprise_alias'] = self.enterprise_alias
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEnterpriseInfoModifyModel()
        if 'enterprise_alias' in d:
            o.enterprise_alias = d['enterprise_alias']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        return o


