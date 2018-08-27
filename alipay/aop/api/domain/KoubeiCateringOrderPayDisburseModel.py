#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderPayDisburseModel(object):

    def __init__(self):
        self._auth_code = None
        self._member_flag = None
        self._out_pay_no = None
        self._pos_order_key = None
        self._timeout = None
        self._total_amount = None
        self._undiscountable = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def member_flag(self):
        return self._member_flag

    @member_flag.setter
    def member_flag(self, value):
        self._member_flag = value
    @property
    def out_pay_no(self):
        return self._out_pay_no

    @out_pay_no.setter
    def out_pay_no(self, value):
        self._out_pay_no = value
    @property
    def pos_order_key(self):
        return self._pos_order_key

    @pos_order_key.setter
    def pos_order_key(self, value):
        if isinstance(value, PosOrderKey):
            self._pos_order_key = value
        else:
            self._pos_order_key = PosOrderKey.from_alipay_dict(value)
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def undiscountable(self):
        return self._undiscountable

    @undiscountable.setter
    def undiscountable(self, value):
        self._undiscountable = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.member_flag:
            if hasattr(self.member_flag, 'to_alipay_dict'):
                params['member_flag'] = self.member_flag.to_alipay_dict()
            else:
                params['member_flag'] = self.member_flag
        if self.out_pay_no:
            if hasattr(self.out_pay_no, 'to_alipay_dict'):
                params['out_pay_no'] = self.out_pay_no.to_alipay_dict()
            else:
                params['out_pay_no'] = self.out_pay_no
        if self.pos_order_key:
            if hasattr(self.pos_order_key, 'to_alipay_dict'):
                params['pos_order_key'] = self.pos_order_key.to_alipay_dict()
            else:
                params['pos_order_key'] = self.pos_order_key
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.undiscountable:
            if hasattr(self.undiscountable, 'to_alipay_dict'):
                params['undiscountable'] = self.undiscountable.to_alipay_dict()
            else:
                params['undiscountable'] = self.undiscountable
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderPayDisburseModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'member_flag' in d:
            o.member_flag = d['member_flag']
        if 'out_pay_no' in d:
            o.out_pay_no = d['out_pay_no']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        if 'timeout' in d:
            o.timeout = d['timeout']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable' in d:
            o.undiscountable = d['undiscountable']
        return o


