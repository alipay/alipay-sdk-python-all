#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistCarfinauctionApplyloanNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._file_id = None
        self._final_down_payment_amount = None
        self._final_down_payment_time = None
        self._out_order_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def final_down_payment_amount(self):
        return self._final_down_payment_amount

    @final_down_payment_amount.setter
    def final_down_payment_amount(self, value):
        self._final_down_payment_amount = value
    @property
    def final_down_payment_time(self):
        return self._final_down_payment_time

    @final_down_payment_time.setter
    def final_down_payment_time(self, value):
        self._final_down_payment_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.final_down_payment_amount:
            if hasattr(self.final_down_payment_amount, 'to_alipay_dict'):
                params['final_down_payment_amount'] = self.final_down_payment_amount.to_alipay_dict()
            else:
                params['final_down_payment_amount'] = self.final_down_payment_amount
        if self.final_down_payment_time:
            if hasattr(self.final_down_payment_time, 'to_alipay_dict'):
                params['final_down_payment_time'] = self.final_down_payment_time.to_alipay_dict()
            else:
                params['final_down_payment_time'] = self.final_down_payment_time
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinauctionApplyloanNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'final_down_payment_amount' in d:
            o.final_down_payment_amount = d['final_down_payment_amount']
        if 'final_down_payment_time' in d:
            o.final_down_payment_time = d['final_down_payment_time']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


