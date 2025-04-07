#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleDeductQueryVO(object):

    def __init__(self):
        self._bind_status = None
        self._bind_wallet_id = None
        self._bind_wallet_type = None
        self._merchant_open_id = None
        self._merchant_pid = None
        self._second_merchant_open_id = None
        self._second_merchant_pid = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
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
    def merchant_open_id(self):
        return self._merchant_open_id

    @merchant_open_id.setter
    def merchant_open_id(self, value):
        self._merchant_open_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
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
        if self.bind_status:
            if hasattr(self.bind_status, 'to_alipay_dict'):
                params['bind_status'] = self.bind_status.to_alipay_dict()
            else:
                params['bind_status'] = self.bind_status
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
        if self.merchant_open_id:
            if hasattr(self.merchant_open_id, 'to_alipay_dict'):
                params['merchant_open_id'] = self.merchant_open_id.to_alipay_dict()
            else:
                params['merchant_open_id'] = self.merchant_open_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
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
        o = RecycleDeductQueryVO()
        if 'bind_status' in d:
            o.bind_status = d['bind_status']
        if 'bind_wallet_id' in d:
            o.bind_wallet_id = d['bind_wallet_id']
        if 'bind_wallet_type' in d:
            o.bind_wallet_type = d['bind_wallet_type']
        if 'merchant_open_id' in d:
            o.merchant_open_id = d['merchant_open_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'second_merchant_open_id' in d:
            o.second_merchant_open_id = d['second_merchant_open_id']
        if 'second_merchant_pid' in d:
            o.second_merchant_pid = d['second_merchant_pid']
        return o


