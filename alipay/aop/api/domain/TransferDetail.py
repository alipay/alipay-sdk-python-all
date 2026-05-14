#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferDetail(object):

    def __init__(self):
        self._amount = None
        self._memo = None
        self._out_request_no = None
        self._payee_inst_id = None
        self._payee_name = None
        self._payee_wallet_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def payee_inst_id(self):
        return self._payee_inst_id

    @payee_inst_id.setter
    def payee_inst_id(self, value):
        self._payee_inst_id = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_wallet_id(self):
        return self._payee_wallet_id

    @payee_wallet_id.setter
    def payee_wallet_id(self, value):
        self._payee_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.payee_inst_id:
            if hasattr(self.payee_inst_id, 'to_alipay_dict'):
                params['payee_inst_id'] = self.payee_inst_id.to_alipay_dict()
            else:
                params['payee_inst_id'] = self.payee_inst_id
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payee_wallet_id:
            if hasattr(self.payee_wallet_id, 'to_alipay_dict'):
                params['payee_wallet_id'] = self.payee_wallet_id.to_alipay_dict()
            else:
                params['payee_wallet_id'] = self.payee_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'payee_inst_id' in d:
            o.payee_inst_id = d['payee_inst_id']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_wallet_id' in d:
            o.payee_wallet_id = d['payee_wallet_id']
        return o


