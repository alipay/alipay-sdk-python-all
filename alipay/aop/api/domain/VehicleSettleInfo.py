#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleSettleInfo(object):

    def __init__(self):
        self._amount = None
        self._summary_dimension = None
        self._trans_in = None
        self._trans_in_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def summary_dimension(self):
        return self._summary_dimension

    @summary_dimension.setter
    def summary_dimension(self, value):
        self._summary_dimension = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.summary_dimension:
            if hasattr(self.summary_dimension, 'to_alipay_dict'):
                params['summary_dimension'] = self.summary_dimension.to_alipay_dict()
            else:
                params['summary_dimension'] = self.summary_dimension
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleSettleInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'summary_dimension' in d:
            o.summary_dimension = d['summary_dimension']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        return o


