#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTerminalPowerbankorderInitializeModel(object):

    def __init__(self):
        self._auth_id = None
        self._out_trade_id = None
        self._sn = None
        self._user_id = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def out_trade_id(self):
        return self._out_trade_id

    @out_trade_id.setter
    def out_trade_id(self, value):
        self._out_trade_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_id:
            if hasattr(self.auth_id, 'to_alipay_dict'):
                params['auth_id'] = self.auth_id.to_alipay_dict()
            else:
                params['auth_id'] = self.auth_id
        if self.out_trade_id:
            if hasattr(self.out_trade_id, 'to_alipay_dict'):
                params['out_trade_id'] = self.out_trade_id.to_alipay_dict()
            else:
                params['out_trade_id'] = self.out_trade_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
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
        o = AlipayCommerceOperationTerminalPowerbankorderInitializeModel()
        if 'auth_id' in d:
            o.auth_id = d['auth_id']
        if 'out_trade_id' in d:
            o.out_trade_id = d['out_trade_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


