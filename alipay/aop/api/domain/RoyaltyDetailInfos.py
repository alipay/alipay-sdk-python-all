#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoyaltyDetailInfos(object):

    def __init__(self):
        self._amount = None
        self._amount_percentage = None
        self._batch_no = None
        self._desc = None
        self._out_relation_id = None
        self._serial_no = None
        self._trans_in = None
        self._trans_in_type = None
        self._trans_out = None
        self._trans_out_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_percentage(self):
        return self._amount_percentage

    @amount_percentage.setter
    def amount_percentage(self, value):
        self._amount_percentage = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def out_relation_id(self):
        return self._out_relation_id

    @out_relation_id.setter
    def out_relation_id(self, value):
        self._out_relation_id = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_in_type(self):
        return self._trans_in_type

    @trans_in_type.setter
    def trans_in_type(self, value):
        self._trans_in_type = value
    @property
    def trans_out(self):
        return self._trans_out

    @trans_out.setter
    def trans_out(self, value):
        self._trans_out = value
    @property
    def trans_out_type(self):
        return self._trans_out_type

    @trans_out_type.setter
    def trans_out_type(self, value):
        self._trans_out_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_percentage:
            if hasattr(self.amount_percentage, 'to_alipay_dict'):
                params['amount_percentage'] = self.amount_percentage.to_alipay_dict()
            else:
                params['amount_percentage'] = self.amount_percentage
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.out_relation_id:
            if hasattr(self.out_relation_id, 'to_alipay_dict'):
                params['out_relation_id'] = self.out_relation_id.to_alipay_dict()
            else:
                params['out_relation_id'] = self.out_relation_id
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_in_type:
            if hasattr(self.trans_in_type, 'to_alipay_dict'):
                params['trans_in_type'] = self.trans_in_type.to_alipay_dict()
            else:
                params['trans_in_type'] = self.trans_in_type
        if self.trans_out:
            if hasattr(self.trans_out, 'to_alipay_dict'):
                params['trans_out'] = self.trans_out.to_alipay_dict()
            else:
                params['trans_out'] = self.trans_out
        if self.trans_out_type:
            if hasattr(self.trans_out_type, 'to_alipay_dict'):
                params['trans_out_type'] = self.trans_out_type.to_alipay_dict()
            else:
                params['trans_out_type'] = self.trans_out_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoyaltyDetailInfos()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_percentage' in d:
            o.amount_percentage = d['amount_percentage']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'desc' in d:
            o.desc = d['desc']
        if 'out_relation_id' in d:
            o.out_relation_id = d['out_relation_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        if 'trans_out' in d:
            o.trans_out = d['trans_out']
        if 'trans_out_type' in d:
            o.trans_out_type = d['trans_out_type']
        return o


