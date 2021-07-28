#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankInfo import BankInfo
from alipay.aop.api.domain.UserIdentity import UserIdentity


class HuanxuTradeAccountserviceCardCertifyModel(object):

    def __init__(self):
        self._bank_info = None
        self._certify_request_no = None
        self._trade_type = None
        self._user_info = None
        self._user_type = None
        self._validate_amount = None

    @property
    def bank_info(self):
        return self._bank_info

    @bank_info.setter
    def bank_info(self, value):
        if isinstance(value, BankInfo):
            self._bank_info = value
        else:
            self._bank_info = BankInfo.from_alipay_dict(value)
    @property
    def certify_request_no(self):
        return self._certify_request_no

    @certify_request_no.setter
    def certify_request_no(self, value):
        self._certify_request_no = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, UserIdentity):
            self._user_info = value
        else:
            self._user_info = UserIdentity.from_alipay_dict(value)
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value
    @property
    def validate_amount(self):
        return self._validate_amount

    @validate_amount.setter
    def validate_amount(self, value):
        self._validate_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_info:
            if hasattr(self.bank_info, 'to_alipay_dict'):
                params['bank_info'] = self.bank_info.to_alipay_dict()
            else:
                params['bank_info'] = self.bank_info
        if self.certify_request_no:
            if hasattr(self.certify_request_no, 'to_alipay_dict'):
                params['certify_request_no'] = self.certify_request_no.to_alipay_dict()
            else:
                params['certify_request_no'] = self.certify_request_no
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        if self.validate_amount:
            if hasattr(self.validate_amount, 'to_alipay_dict'):
                params['validate_amount'] = self.validate_amount.to_alipay_dict()
            else:
                params['validate_amount'] = self.validate_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HuanxuTradeAccountserviceCardCertifyModel()
        if 'bank_info' in d:
            o.bank_info = d['bank_info']
        if 'certify_request_no' in d:
            o.certify_request_no = d['certify_request_no']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'user_info' in d:
            o.user_info = d['user_info']
        if 'user_type' in d:
            o.user_type = d['user_type']
        if 'validate_amount' in d:
            o.validate_amount = d['validate_amount']
        return o


