#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleDeductRelationSaveModel(object):

    def __init__(self):
        self._bind_wallet_id = None
        self._bind_wallet_type = None
        self._handle_type = None
        self._second_merchant_open_id = None
        self._second_merchant_pid = None

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
    @property
    def handle_type(self):
        return self._handle_type

    @handle_type.setter
    def handle_type(self, value):
        self._handle_type = value
    @property
    def second_merchant_open_id(self):
        return self._second_merchant_open_id

    @second_merchant_open_id.setter
    def second_merchant_open_id(self, value):
        self._second_merchant_open_id = value
    @property
    def second_merchant_pid(self):
        return self._second_merchant_pid

    @second_merchant_pid.setter
    def second_merchant_pid(self, value):
        self._second_merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.handle_type:
            if hasattr(self.handle_type, 'to_alipay_dict'):
                params['handle_type'] = self.handle_type.to_alipay_dict()
            else:
                params['handle_type'] = self.handle_type
        if self.second_merchant_open_id:
            if hasattr(self.second_merchant_open_id, 'to_alipay_dict'):
                params['second_merchant_open_id'] = self.second_merchant_open_id.to_alipay_dict()
            else:
                params['second_merchant_open_id'] = self.second_merchant_open_id
        if self.second_merchant_pid:
            if hasattr(self.second_merchant_pid, 'to_alipay_dict'):
                params['second_merchant_pid'] = self.second_merchant_pid.to_alipay_dict()
            else:
                params['second_merchant_pid'] = self.second_merchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleDeductRelationSaveModel()
        if 'bind_wallet_id' in d:
            o.bind_wallet_id = d['bind_wallet_id']
        if 'bind_wallet_type' in d:
            o.bind_wallet_type = d['bind_wallet_type']
        if 'handle_type' in d:
            o.handle_type = d['handle_type']
        if 'second_merchant_open_id' in d:
            o.second_merchant_open_id = d['second_merchant_open_id']
        if 'second_merchant_pid' in d:
            o.second_merchant_pid = d['second_merchant_pid']
        return o


