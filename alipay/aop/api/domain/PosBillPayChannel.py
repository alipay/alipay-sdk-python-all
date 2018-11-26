#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosDiscountDetail import PosDiscountDetail


class PosBillPayChannel(object):

    def __init__(self):
        self._channel_type = None
        self._discount_details = None
        self._ext_info = None
        self._operator = None
        self._out_pay_no = None
        self._pay_amount = None
        self._pay_no = None
        self._pay_time = None
        self._receipt_amount = None
        self._trade_no = None
        self._user_identity = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def discount_details(self):
        return self._discount_details

    @discount_details.setter
    def discount_details(self, value):
        if isinstance(value, list):
            self._discount_details = list()
            for i in value:
                if isinstance(i, PosDiscountDetail):
                    self._discount_details.append(i)
                else:
                    self._discount_details.append(PosDiscountDetail.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_pay_no(self):
        return self._out_pay_no

    @out_pay_no.setter
    def out_pay_no(self, value):
        self._out_pay_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_identity(self):
        return self._user_identity

    @user_identity.setter
    def user_identity(self, value):
        self._user_identity = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.discount_details:
            if isinstance(self.discount_details, list):
                for i in range(0, len(self.discount_details)):
                    element = self.discount_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_details[i] = element.to_alipay_dict()
            if hasattr(self.discount_details, 'to_alipay_dict'):
                params['discount_details'] = self.discount_details.to_alipay_dict()
            else:
                params['discount_details'] = self.discount_details
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_pay_no:
            if hasattr(self.out_pay_no, 'to_alipay_dict'):
                params['out_pay_no'] = self.out_pay_no.to_alipay_dict()
            else:
                params['out_pay_no'] = self.out_pay_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_no:
            if hasattr(self.pay_no, 'to_alipay_dict'):
                params['pay_no'] = self.pay_no.to_alipay_dict()
            else:
                params['pay_no'] = self.pay_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_identity:
            if hasattr(self.user_identity, 'to_alipay_dict'):
                params['user_identity'] = self.user_identity.to_alipay_dict()
            else:
                params['user_identity'] = self.user_identity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosBillPayChannel()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'discount_details' in d:
            o.discount_details = d['discount_details']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_pay_no' in d:
            o.out_pay_no = d['out_pay_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_no' in d:
            o.pay_no = d['pay_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_identity' in d:
            o.user_identity = d['user_identity']
        return o


