#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotAccountbindingCreateModel(object):

    def __init__(self):
        self._protocol_supplier_id = None
        self._protocol_user_id = None
        self._protocol_user_name = None
        self._user_id = None

    @property
    def protocol_supplier_id(self):
        return self._protocol_supplier_id

    @protocol_supplier_id.setter
    def protocol_supplier_id(self, value):
        self._protocol_supplier_id = value
    @property
    def protocol_user_id(self):
        return self._protocol_user_id

    @protocol_user_id.setter
    def protocol_user_id(self, value):
        self._protocol_user_id = value
    @property
    def protocol_user_name(self):
        return self._protocol_user_name

    @protocol_user_name.setter
    def protocol_user_name(self, value):
        self._protocol_user_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.protocol_supplier_id:
            if hasattr(self.protocol_supplier_id, 'to_alipay_dict'):
                params['protocol_supplier_id'] = self.protocol_supplier_id.to_alipay_dict()
            else:
                params['protocol_supplier_id'] = self.protocol_supplier_id
        if self.protocol_user_id:
            if hasattr(self.protocol_user_id, 'to_alipay_dict'):
                params['protocol_user_id'] = self.protocol_user_id.to_alipay_dict()
            else:
                params['protocol_user_id'] = self.protocol_user_id
        if self.protocol_user_name:
            if hasattr(self.protocol_user_name, 'to_alipay_dict'):
                params['protocol_user_name'] = self.protocol_user_name.to_alipay_dict()
            else:
                params['protocol_user_name'] = self.protocol_user_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotAccountbindingCreateModel()
        if 'protocol_supplier_id' in d:
            o.protocol_supplier_id = d['protocol_supplier_id']
        if 'protocol_user_id' in d:
            o.protocol_user_id = d['protocol_user_id']
        if 'protocol_user_name' in d:
            o.protocol_user_name = d['protocol_user_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


