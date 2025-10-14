#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PurchaseInfo(object):

    def __init__(self):
        self._bind_wallet_id = None
        self._bind_wallet_type = None
        self._pay_relation_openid = None
        self._pay_relation_uid = None

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
    def pay_relation_openid(self):
        return self._pay_relation_openid

    @pay_relation_openid.setter
    def pay_relation_openid(self, value):
        self._pay_relation_openid = value
    @property
    def pay_relation_uid(self):
        return self._pay_relation_uid

    @pay_relation_uid.setter
    def pay_relation_uid(self, value):
        self._pay_relation_uid = value


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
        if self.pay_relation_openid:
            if hasattr(self.pay_relation_openid, 'to_alipay_dict'):
                params['pay_relation_openid'] = self.pay_relation_openid.to_alipay_dict()
            else:
                params['pay_relation_openid'] = self.pay_relation_openid
        if self.pay_relation_uid:
            if hasattr(self.pay_relation_uid, 'to_alipay_dict'):
                params['pay_relation_uid'] = self.pay_relation_uid.to_alipay_dict()
            else:
                params['pay_relation_uid'] = self.pay_relation_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseInfo()
        if 'bind_wallet_id' in d:
            o.bind_wallet_id = d['bind_wallet_id']
        if 'bind_wallet_type' in d:
            o.bind_wallet_type = d['bind_wallet_type']
        if 'pay_relation_openid' in d:
            o.pay_relation_openid = d['pay_relation_openid']
        if 'pay_relation_uid' in d:
            o.pay_relation_uid = d['pay_relation_uid']
        return o


