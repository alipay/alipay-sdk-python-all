#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantMemberwalletWalletQueryModel(object):

    def __init__(self):
        self._member_wallet_id = None
        self._out_user_id = None

    @property
    def member_wallet_id(self):
        return self._member_wallet_id

    @member_wallet_id.setter
    def member_wallet_id(self, value):
        self._member_wallet_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_wallet_id:
            if hasattr(self.member_wallet_id, 'to_alipay_dict'):
                params['member_wallet_id'] = self.member_wallet_id.to_alipay_dict()
            else:
                params['member_wallet_id'] = self.member_wallet_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantMemberwalletWalletQueryModel()
        if 'member_wallet_id' in d:
            o.member_wallet_id = d['member_wallet_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        return o


