#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeSettleDetail(object):

    def __init__(self):
        self._amount = None
        self._operation_dt = None
        self._operation_serial_no = None
        self._operation_type = None
        self._ori_trans_in = None
        self._ori_trans_out = None
        self._trans_in = None
        self._trans_out = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def operation_dt(self):
        return self._operation_dt

    @operation_dt.setter
    def operation_dt(self, value):
        self._operation_dt = value
    @property
    def operation_serial_no(self):
        return self._operation_serial_no

    @operation_serial_no.setter
    def operation_serial_no(self, value):
        self._operation_serial_no = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def ori_trans_in(self):
        return self._ori_trans_in

    @ori_trans_in.setter
    def ori_trans_in(self, value):
        self._ori_trans_in = value
    @property
    def ori_trans_out(self):
        return self._ori_trans_out

    @ori_trans_out.setter
    def ori_trans_out(self, value):
        self._ori_trans_out = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_out(self):
        return self._trans_out

    @trans_out.setter
    def trans_out(self, value):
        self._trans_out = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.operation_dt:
            if hasattr(self.operation_dt, 'to_alipay_dict'):
                params['operation_dt'] = self.operation_dt.to_alipay_dict()
            else:
                params['operation_dt'] = self.operation_dt
        if self.operation_serial_no:
            if hasattr(self.operation_serial_no, 'to_alipay_dict'):
                params['operation_serial_no'] = self.operation_serial_no.to_alipay_dict()
            else:
                params['operation_serial_no'] = self.operation_serial_no
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.ori_trans_in:
            if hasattr(self.ori_trans_in, 'to_alipay_dict'):
                params['ori_trans_in'] = self.ori_trans_in.to_alipay_dict()
            else:
                params['ori_trans_in'] = self.ori_trans_in
        if self.ori_trans_out:
            if hasattr(self.ori_trans_out, 'to_alipay_dict'):
                params['ori_trans_out'] = self.ori_trans_out.to_alipay_dict()
            else:
                params['ori_trans_out'] = self.ori_trans_out
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_out:
            if hasattr(self.trans_out, 'to_alipay_dict'):
                params['trans_out'] = self.trans_out.to_alipay_dict()
            else:
                params['trans_out'] = self.trans_out
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeSettleDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'operation_dt' in d:
            o.operation_dt = d['operation_dt']
        if 'operation_serial_no' in d:
            o.operation_serial_no = d['operation_serial_no']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'ori_trans_in' in d:
            o.ori_trans_in = d['ori_trans_in']
        if 'ori_trans_out' in d:
            o.ori_trans_out = d['ori_trans_out']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_out' in d:
            o.trans_out = d['trans_out']
        return o


