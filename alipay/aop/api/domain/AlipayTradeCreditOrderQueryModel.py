#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCreditOrderQueryModel(object):

    def __init__(self):
        self._credit_biz_order_id = None
        self._out_trade_no = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_biz_order_id:
            if hasattr(self.credit_biz_order_id, 'to_alipay_dict'):
                params['credit_biz_order_id'] = self.credit_biz_order_id.to_alipay_dict()
            else:
                params['credit_biz_order_id'] = self.credit_biz_order_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCreditOrderQueryModel()
        if 'credit_biz_order_id' in d:
            o.credit_biz_order_id = d['credit_biz_order_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        return o


