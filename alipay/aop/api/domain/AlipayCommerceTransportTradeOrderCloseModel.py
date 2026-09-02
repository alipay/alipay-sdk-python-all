#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTradeOrderCloseModel(object):

    def __init__(self):
        self._bill_no = None
        self._merchant_biz_type = None
        self._open_id = None
        self._out_biz_no = None
        self._out_sub_biz_no = None
        self._trade_no = None
        self._user_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_sub_biz_no(self):
        return self._out_sub_biz_no

    @out_sub_biz_no.setter
    def out_sub_biz_no(self, value):
        self._out_sub_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.merchant_biz_type:
            if hasattr(self.merchant_biz_type, 'to_alipay_dict'):
                params['merchant_biz_type'] = self.merchant_biz_type.to_alipay_dict()
            else:
                params['merchant_biz_type'] = self.merchant_biz_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_sub_biz_no:
            if hasattr(self.out_sub_biz_no, 'to_alipay_dict'):
                params['out_sub_biz_no'] = self.out_sub_biz_no.to_alipay_dict()
            else:
                params['out_sub_biz_no'] = self.out_sub_biz_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTradeOrderCloseModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_sub_biz_no' in d:
            o.out_sub_biz_no = d['out_sub_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


