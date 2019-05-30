#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomsDeclareBuyerInfo import CustomsDeclareBuyerInfo


class AlipayTradeCustomsDeclareModel(object):

    def __init__(self):
        self._amount = None
        self._buyer_info = None
        self._customs_place = None
        self._declare_mode = None
        self._is_split = None
        self._merchant_customs_code = None
        self._merchant_customs_name = None
        self._out_request_no = None
        self._sub_out_biz_no = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, CustomsDeclareBuyerInfo):
            self._buyer_info = value
        else:
            self._buyer_info = CustomsDeclareBuyerInfo.from_alipay_dict(value)
    @property
    def customs_place(self):
        return self._customs_place

    @customs_place.setter
    def customs_place(self, value):
        self._customs_place = value
    @property
    def declare_mode(self):
        return self._declare_mode

    @declare_mode.setter
    def declare_mode(self, value):
        self._declare_mode = value
    @property
    def is_split(self):
        return self._is_split

    @is_split.setter
    def is_split(self, value):
        self._is_split = value
    @property
    def merchant_customs_code(self):
        return self._merchant_customs_code

    @merchant_customs_code.setter
    def merchant_customs_code(self, value):
        self._merchant_customs_code = value
    @property
    def merchant_customs_name(self):
        return self._merchant_customs_name

    @merchant_customs_name.setter
    def merchant_customs_name(self, value):
        self._merchant_customs_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def sub_out_biz_no(self):
        return self._sub_out_biz_no

    @sub_out_biz_no.setter
    def sub_out_biz_no(self, value):
        self._sub_out_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.customs_place:
            if hasattr(self.customs_place, 'to_alipay_dict'):
                params['customs_place'] = self.customs_place.to_alipay_dict()
            else:
                params['customs_place'] = self.customs_place
        if self.declare_mode:
            if hasattr(self.declare_mode, 'to_alipay_dict'):
                params['declare_mode'] = self.declare_mode.to_alipay_dict()
            else:
                params['declare_mode'] = self.declare_mode
        if self.is_split:
            if hasattr(self.is_split, 'to_alipay_dict'):
                params['is_split'] = self.is_split.to_alipay_dict()
            else:
                params['is_split'] = self.is_split
        if self.merchant_customs_code:
            if hasattr(self.merchant_customs_code, 'to_alipay_dict'):
                params['merchant_customs_code'] = self.merchant_customs_code.to_alipay_dict()
            else:
                params['merchant_customs_code'] = self.merchant_customs_code
        if self.merchant_customs_name:
            if hasattr(self.merchant_customs_name, 'to_alipay_dict'):
                params['merchant_customs_name'] = self.merchant_customs_name.to_alipay_dict()
            else:
                params['merchant_customs_name'] = self.merchant_customs_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.sub_out_biz_no:
            if hasattr(self.sub_out_biz_no, 'to_alipay_dict'):
                params['sub_out_biz_no'] = self.sub_out_biz_no.to_alipay_dict()
            else:
                params['sub_out_biz_no'] = self.sub_out_biz_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCustomsDeclareModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'customs_place' in d:
            o.customs_place = d['customs_place']
        if 'declare_mode' in d:
            o.declare_mode = d['declare_mode']
        if 'is_split' in d:
            o.is_split = d['is_split']
        if 'merchant_customs_code' in d:
            o.merchant_customs_code = d['merchant_customs_code']
        if 'merchant_customs_name' in d:
            o.merchant_customs_name = d['merchant_customs_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'sub_out_biz_no' in d:
            o.sub_out_biz_no = d['sub_out_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


