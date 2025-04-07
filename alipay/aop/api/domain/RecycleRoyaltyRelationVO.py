#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleRoyaltyRelationVO(object):

    def __init__(self):
        self._bind_role_id = None
        self._bind_role_type = None
        self._bind_wallet_id = None
        self._bind_wallet_type = None

    @property
    def bind_role_id(self):
        return self._bind_role_id

    @bind_role_id.setter
    def bind_role_id(self, value):
        self._bind_role_id = value
    @property
    def bind_role_type(self):
        return self._bind_role_type

    @bind_role_type.setter
    def bind_role_type(self, value):
        self._bind_role_type = value
    @property
    def bind_wallet_id(self):
        return self._bind_wallet_id

    @bind_wallet_id.setter
    def bind_wallet_id(self, value):
        self._bind_wallet_id = value
    @property
    def bind_wallet_type(self):
        return self._bind_wallet_type

    @bind_wallet_type.setter
    def bind_wallet_type(self, value):
        self._bind_wallet_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_role_id:
            if hasattr(self.bind_role_id, 'to_alipay_dict'):
                params['bind_role_id'] = self.bind_role_id.to_alipay_dict()
            else:
                params['bind_role_id'] = self.bind_role_id
        if self.bind_role_type:
            if hasattr(self.bind_role_type, 'to_alipay_dict'):
                params['bind_role_type'] = self.bind_role_type.to_alipay_dict()
            else:
                params['bind_role_type'] = self.bind_role_type
        if self.bind_wallet_id:
            if hasattr(self.bind_wallet_id, 'to_alipay_dict'):
                params['bind_wallet_id'] = self.bind_wallet_id.to_alipay_dict()
            else:
                params['bind_wallet_id'] = self.bind_wallet_id
        if self.bind_wallet_type:
            if hasattr(self.bind_wallet_type, 'to_alipay_dict'):
                params['bind_wallet_type'] = self.bind_wallet_type.to_alipay_dict()
            else:
                params['bind_wallet_type'] = self.bind_wallet_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleRoyaltyRelationVO()
        if 'bind_role_id' in d:
            o.bind_role_id = d['bind_role_id']
        if 'bind_role_type' in d:
            o.bind_role_type = d['bind_role_type']
        if 'bind_wallet_id' in d:
            o.bind_wallet_id = d['bind_wallet_id']
        if 'bind_wallet_type' in d:
            o.bind_wallet_type = d['bind_wallet_type']
        return o


