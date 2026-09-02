#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResaleFundInfoVO(object):

    def __init__(self):
        self._amount = None
        self._out_request_id = None
        self._trade_memo = None
        self._trade_no = None
        self._trade_prop = None
        self._trade_status = None
        self._trade_sub_type = None
        self._trade_time = None
        self._trade_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def trade_memo(self):
        return self._trade_memo

    @trade_memo.setter
    def trade_memo(self, value):
        self._trade_memo = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_prop(self):
        return self._trade_prop

    @trade_prop.setter
    def trade_prop(self, value):
        self._trade_prop = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trade_sub_type(self):
        return self._trade_sub_type

    @trade_sub_type.setter
    def trade_sub_type(self, value):
        self._trade_sub_type = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.trade_memo:
            if hasattr(self.trade_memo, 'to_alipay_dict'):
                params['trade_memo'] = self.trade_memo.to_alipay_dict()
            else:
                params['trade_memo'] = self.trade_memo
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_prop:
            if hasattr(self.trade_prop, 'to_alipay_dict'):
                params['trade_prop'] = self.trade_prop.to_alipay_dict()
            else:
                params['trade_prop'] = self.trade_prop
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
        if self.trade_sub_type:
            if hasattr(self.trade_sub_type, 'to_alipay_dict'):
                params['trade_sub_type'] = self.trade_sub_type.to_alipay_dict()
            else:
                params['trade_sub_type'] = self.trade_sub_type
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResaleFundInfoVO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'trade_memo' in d:
            o.trade_memo = d['trade_memo']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_prop' in d:
            o.trade_prop = d['trade_prop']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        if 'trade_sub_type' in d:
            o.trade_sub_type = d['trade_sub_type']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


