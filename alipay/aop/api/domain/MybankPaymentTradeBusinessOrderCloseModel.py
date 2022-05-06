#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeBusinessOrderCloseModel(object):

    def __init__(self):
        self._order_no = None
        self._out_trade_no = None
        self._user_info_id = None
        self._user_info_type = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def user_info_id(self):
        return self._user_info_id

    @user_info_id.setter
    def user_info_id(self, value):
        self._user_info_id = value
    @property
    def user_info_type(self):
        return self._user_info_type

    @user_info_type.setter
    def user_info_type(self, value):
        self._user_info_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.user_info_id:
            if hasattr(self.user_info_id, 'to_alipay_dict'):
                params['user_info_id'] = self.user_info_id.to_alipay_dict()
            else:
                params['user_info_id'] = self.user_info_id
        if self.user_info_type:
            if hasattr(self.user_info_type, 'to_alipay_dict'):
                params['user_info_type'] = self.user_info_type.to_alipay_dict()
            else:
                params['user_info_type'] = self.user_info_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeBusinessOrderCloseModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'user_info_id' in d:
            o.user_info_id = d['user_info_id']
        if 'user_info_type' in d:
            o.user_info_type = d['user_info_type']
        return o


