#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantMemberwalletBalanceQueryModel(object):

    def __init__(self):
        self._member_wallet_id = None
        self._wallet_id = None

    @property
    def member_wallet_id(self):
        return self._member_wallet_id

    @member_wallet_id.setter
    def member_wallet_id(self, value):
        self._member_wallet_id = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_wallet_id:
            if hasattr(self.member_wallet_id, 'to_alipay_dict'):
                params['member_wallet_id'] = self.member_wallet_id.to_alipay_dict()
            else:
                params['member_wallet_id'] = self.member_wallet_id
        if self.wallet_id:
            if hasattr(self.wallet_id, 'to_alipay_dict'):
                params['wallet_id'] = self.wallet_id.to_alipay_dict()
            else:
                params['wallet_id'] = self.wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantMemberwalletBalanceQueryModel()
        if 'member_wallet_id' in d:
            o.member_wallet_id = d['member_wallet_id']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        return o


