#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleDetailInfo(object):

    def __init__(self):
        self._amount = None
        self._settle_entity_id = None
        self._settle_entity_type = None
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
    def settle_entity_id(self):
        return self._settle_entity_id

    @settle_entity_id.setter
    def settle_entity_id(self, value):
        self._settle_entity_id = value
    @property
    def settle_entity_type(self):
        return self._settle_entity_type

    @settle_entity_type.setter
    def settle_entity_type(self, value):
        self._settle_entity_type = value
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
        if self.settle_entity_id:
            if hasattr(self.settle_entity_id, 'to_alipay_dict'):
                params['settle_entity_id'] = self.settle_entity_id.to_alipay_dict()
            else:
                params['settle_entity_id'] = self.settle_entity_id
        if self.settle_entity_type:
            if hasattr(self.settle_entity_type, 'to_alipay_dict'):
                params['settle_entity_type'] = self.settle_entity_type.to_alipay_dict()
            else:
                params['settle_entity_type'] = self.settle_entity_type
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
        o = SettleDetailInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'settle_entity_id' in d:
            o.settle_entity_id = d['settle_entity_id']
        if 'settle_entity_type' in d:
            o.settle_entity_type = d['settle_entity_type']
        if 'summary_dimension' in d:
            o.summary_dimension = d['summary_dimension']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        return o


