#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConfirmSettleDetailInfo(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._amount = None
        self._settle_entity_id = None
        self._settle_entity_type = None
        self._trans_in = None
        self._trans_in_type = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
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
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
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
        o = ConfirmSettleDetailInfo()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'settle_entity_id' in d:
            o.settle_entity_id = d['settle_entity_id']
        if 'settle_entity_type' in d:
            o.settle_entity_type = d['settle_entity_type']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        return o


