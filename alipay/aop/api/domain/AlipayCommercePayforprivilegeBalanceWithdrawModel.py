#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePayforprivilegeBalanceWithdrawModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._user_id = None
        self._withdraw_amount = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def withdraw_amount(self):
        return self._withdraw_amount

    @withdraw_amount.setter
    def withdraw_amount(self, value):
        self._withdraw_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
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
        o = AlipayCommercePayforprivilegeBalanceWithdrawModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'withdraw_amount' in d:
            o.withdraw_amount = d['withdraw_amount']
        return o


