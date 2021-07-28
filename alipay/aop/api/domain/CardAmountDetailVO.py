#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardAmountDetailVO(object):

    def __init__(self):
        self._amount = None
        self._card_holder_name = None
        self._out_bank_card_no = None
        self._out_bank_inst_id = None
        self._out_bank_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def card_holder_name(self):
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value):
        self._card_holder_name = value
    @property
    def out_bank_card_no(self):
        return self._out_bank_card_no

    @out_bank_card_no.setter
    def out_bank_card_no(self, value):
        self._out_bank_card_no = value
    @property
    def out_bank_inst_id(self):
        return self._out_bank_inst_id

    @out_bank_inst_id.setter
    def out_bank_inst_id(self, value):
        self._out_bank_inst_id = value
    @property
    def out_bank_name(self):
        return self._out_bank_name

    @out_bank_name.setter
    def out_bank_name(self, value):
        self._out_bank_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.card_holder_name:
            if hasattr(self.card_holder_name, 'to_alipay_dict'):
                params['card_holder_name'] = self.card_holder_name.to_alipay_dict()
            else:
                params['card_holder_name'] = self.card_holder_name
        if self.out_bank_card_no:
            if hasattr(self.out_bank_card_no, 'to_alipay_dict'):
                params['out_bank_card_no'] = self.out_bank_card_no.to_alipay_dict()
            else:
                params['out_bank_card_no'] = self.out_bank_card_no
        if self.out_bank_inst_id:
            if hasattr(self.out_bank_inst_id, 'to_alipay_dict'):
                params['out_bank_inst_id'] = self.out_bank_inst_id.to_alipay_dict()
            else:
                params['out_bank_inst_id'] = self.out_bank_inst_id
        if self.out_bank_name:
            if hasattr(self.out_bank_name, 'to_alipay_dict'):
                params['out_bank_name'] = self.out_bank_name.to_alipay_dict()
            else:
                params['out_bank_name'] = self.out_bank_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardAmountDetailVO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'card_holder_name' in d:
            o.card_holder_name = d['card_holder_name']
        if 'out_bank_card_no' in d:
            o.out_bank_card_no = d['out_bank_card_no']
        if 'out_bank_inst_id' in d:
            o.out_bank_inst_id = d['out_bank_inst_id']
        if 'out_bank_name' in d:
            o.out_bank_name = d['out_bank_name']
        return o


