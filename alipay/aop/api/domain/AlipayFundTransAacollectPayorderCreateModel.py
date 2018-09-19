#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransAacollectPayorderCreateModel(object):

    def __init__(self):
        self._batch_no = None
        self._batch_token = None
        self._ext_param = None
        self._pay_amount = None
        self._payer_user_id = None
        self._source = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_token(self):
        return self._batch_token

    @batch_token.setter
    def batch_token(self, value):
        self._batch_token = value
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
    def payer_user_id(self):
        return self._payer_user_id

    @payer_user_id.setter
    def payer_user_id(self, value):
        self._payer_user_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.batch_token:
            if hasattr(self.batch_token, 'to_alipay_dict'):
                params['batch_token'] = self.batch_token.to_alipay_dict()
            else:
                params['batch_token'] = self.batch_token
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
        if self.payer_user_id:
            if hasattr(self.payer_user_id, 'to_alipay_dict'):
                params['payer_user_id'] = self.payer_user_id.to_alipay_dict()
            else:
                params['payer_user_id'] = self.payer_user_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransAacollectPayorderCreateModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'batch_token' in d:
            o.batch_token = d['batch_token']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payer_user_id' in d:
            o.payer_user_id = d['payer_user_id']
        if 'source' in d:
            o.source = d['source']
        return o


