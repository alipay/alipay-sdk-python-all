#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantMemberwalletRechargeCreateModel(object):

    def __init__(self):
        self._benefit_amount = None
        self._benefit_validate_date = None
        self._member_wallet_id = None
        self._out_trade_no = None
        self._principal_amount = None
        self._validate_date = None
        self._wallet_id = None

    @property
    def benefit_amount(self):
        return self._benefit_amount

    @benefit_amount.setter
    def benefit_amount(self, value):
        self._benefit_amount = value
    @property
    def benefit_validate_date(self):
        return self._benefit_validate_date

    @benefit_validate_date.setter
    def benefit_validate_date(self, value):
        self._benefit_validate_date = value
    @property
    def member_wallet_id(self):
        return self._member_wallet_id

    @member_wallet_id.setter
    def member_wallet_id(self, value):
        self._member_wallet_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def principal_amount(self):
        return self._principal_amount

    @principal_amount.setter
    def principal_amount(self, value):
        self._principal_amount = value
    @property
    def validate_date(self):
        return self._validate_date

    @validate_date.setter
    def validate_date(self, value):
        self._validate_date = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_amount:
            if hasattr(self.benefit_amount, 'to_alipay_dict'):
                params['benefit_amount'] = self.benefit_amount.to_alipay_dict()
            else:
                params['benefit_amount'] = self.benefit_amount
        if self.benefit_validate_date:
            if hasattr(self.benefit_validate_date, 'to_alipay_dict'):
                params['benefit_validate_date'] = self.benefit_validate_date.to_alipay_dict()
            else:
                params['benefit_validate_date'] = self.benefit_validate_date
        if self.member_wallet_id:
            if hasattr(self.member_wallet_id, 'to_alipay_dict'):
                params['member_wallet_id'] = self.member_wallet_id.to_alipay_dict()
            else:
                params['member_wallet_id'] = self.member_wallet_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.principal_amount:
            if hasattr(self.principal_amount, 'to_alipay_dict'):
                params['principal_amount'] = self.principal_amount.to_alipay_dict()
            else:
                params['principal_amount'] = self.principal_amount
        if self.validate_date:
            if hasattr(self.validate_date, 'to_alipay_dict'):
                params['validate_date'] = self.validate_date.to_alipay_dict()
            else:
                params['validate_date'] = self.validate_date
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
        o = AntMerchantMemberwalletRechargeCreateModel()
        if 'benefit_amount' in d:
            o.benefit_amount = d['benefit_amount']
        if 'benefit_validate_date' in d:
            o.benefit_validate_date = d['benefit_validate_date']
        if 'member_wallet_id' in d:
            o.member_wallet_id = d['member_wallet_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'principal_amount' in d:
            o.principal_amount = d['principal_amount']
        if 'validate_date' in d:
            o.validate_date = d['validate_date']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        return o


