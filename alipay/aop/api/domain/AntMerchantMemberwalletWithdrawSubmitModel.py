#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantMemberwalletWithdrawSubmitModel(object):

    def __init__(self):
        self._member_wallet_id = None
        self._out_biz_no = None
        self._wallet_id = None
        self._withdraw_amount = None

    @property
    def member_wallet_id(self):
        return self._member_wallet_id

    @member_wallet_id.setter
    def member_wallet_id(self, value):
        self._member_wallet_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value
    @property
    def withdraw_amount(self):
        return self._withdraw_amount

    @withdraw_amount.setter
    def withdraw_amount(self, value):
        self._withdraw_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_wallet_id:
            if hasattr(self.member_wallet_id, 'to_alipay_dict'):
                params['member_wallet_id'] = self.member_wallet_id.to_alipay_dict()
            else:
                params['member_wallet_id'] = self.member_wallet_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.wallet_id:
            if hasattr(self.wallet_id, 'to_alipay_dict'):
                params['wallet_id'] = self.wallet_id.to_alipay_dict()
            else:
                params['wallet_id'] = self.wallet_id
        if self.withdraw_amount:
            if hasattr(self.withdraw_amount, 'to_alipay_dict'):
                params['withdraw_amount'] = self.withdraw_amount.to_alipay_dict()
            else:
                params['withdraw_amount'] = self.withdraw_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantMemberwalletWithdrawSubmitModel()
        if 'member_wallet_id' in d:
            o.member_wallet_id = d['member_wallet_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        if 'withdraw_amount' in d:
            o.withdraw_amount = d['withdraw_amount']
        return o


