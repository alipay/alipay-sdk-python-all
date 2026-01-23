#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcTradeIdentityAccountInfo(object):

    def __init__(self):
        self._bind_uid = None
        self._invalid_reason = None
        self._logon_id = None
        self._merchant_name = None
        self._status = None
        self._trade_pid = None
        self._trade_shop_id = None
        self._type = None

    @property
    def bind_uid(self):
        return self._bind_uid

    @bind_uid.setter
    def bind_uid(self, value):
        self._bind_uid = value
    @property
    def invalid_reason(self):
        return self._invalid_reason

    @invalid_reason.setter
    def invalid_reason(self, value):
        self._invalid_reason = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_pid(self):
        return self._trade_pid

    @trade_pid.setter
    def trade_pid(self, value):
        self._trade_pid = value
    @property
    def trade_shop_id(self):
        return self._trade_shop_id

    @trade_shop_id.setter
    def trade_shop_id(self, value):
        self._trade_shop_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_uid:
            if hasattr(self.bind_uid, 'to_alipay_dict'):
                params['bind_uid'] = self.bind_uid.to_alipay_dict()
            else:
                params['bind_uid'] = self.bind_uid
        if self.invalid_reason:
            if hasattr(self.invalid_reason, 'to_alipay_dict'):
                params['invalid_reason'] = self.invalid_reason.to_alipay_dict()
            else:
                params['invalid_reason'] = self.invalid_reason
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_pid:
            if hasattr(self.trade_pid, 'to_alipay_dict'):
                params['trade_pid'] = self.trade_pid.to_alipay_dict()
            else:
                params['trade_pid'] = self.trade_pid
        if self.trade_shop_id:
            if hasattr(self.trade_shop_id, 'to_alipay_dict'):
                params['trade_shop_id'] = self.trade_shop_id.to_alipay_dict()
            else:
                params['trade_shop_id'] = self.trade_shop_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcTradeIdentityAccountInfo()
        if 'bind_uid' in d:
            o.bind_uid = d['bind_uid']
        if 'invalid_reason' in d:
            o.invalid_reason = d['invalid_reason']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'status' in d:
            o.status = d['status']
        if 'trade_pid' in d:
            o.trade_pid = d['trade_pid']
        if 'trade_shop_id' in d:
            o.trade_shop_id = d['trade_shop_id']
        if 'type' in d:
            o.type = d['type']
        return o


