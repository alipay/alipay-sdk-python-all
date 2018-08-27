#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransBatchCreateorderModel(object):

    def __init__(self):
        self._batch_no = None
        self._ext_param = None
        self._pay_amount = None
        self._payee_id = None
        self._payer_id = None
        self._token = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payee_id(self):
        return self._payee_id

    @payee_id.setter
    def payee_id(self, value):
        self._payee_id = value
    @property
    def payer_id(self):
        return self._payer_id

    @payer_id.setter
    def payer_id(self, value):
        self._payer_id = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.payee_id:
            if hasattr(self.payee_id, 'to_alipay_dict'):
                params['payee_id'] = self.payee_id.to_alipay_dict()
            else:
                params['payee_id'] = self.payee_id
        if self.payer_id:
            if hasattr(self.payer_id, 'to_alipay_dict'):
                params['payer_id'] = self.payer_id.to_alipay_dict()
            else:
                params['payer_id'] = self.payer_id
        if self.token:
            if hasattr(self.token, 'to_alipay_dict'):
                params['token'] = self.token.to_alipay_dict()
            else:
                params['token'] = self.token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransBatchCreateorderModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payee_id' in d:
            o.payee_id = d['payee_id']
        if 'payer_id' in d:
            o.payer_id = d['payer_id']
        if 'token' in d:
            o.token = d['token']
        return o


