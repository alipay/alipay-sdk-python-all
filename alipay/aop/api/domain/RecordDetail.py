#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecordDetail(object):

    def __init__(self):
        self._consume_title = None
        self._out_order_no = None
        self._trans_amount = None
        self._trans_dt = None

    @property
    def consume_title(self):
        return self._consume_title

    @consume_title.setter
    def consume_title(self, value):
        self._consume_title = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value


    def to_alipay_dict(self):
        params = dict()
        if self.consume_title:
            if hasattr(self.consume_title, 'to_alipay_dict'):
                params['consume_title'] = self.consume_title.to_alipay_dict()
            else:
                params['consume_title'] = self.consume_title
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecordDetail()
        if 'consume_title' in d:
            o.consume_title = d['consume_title']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        return o


