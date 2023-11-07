#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantSettleRelationProcessorRequest(object):

    def __init__(self):
        self._rate = None
        self._trans_in_account = None
        self._trans_in_name = None

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def trans_in_account(self):
        return self._trans_in_account

    @trans_in_account.setter
    def trans_in_account(self, value):
        self._trans_in_account = value
    @property
    def trans_in_name(self):
        return self._trans_in_name

    @trans_in_name.setter
    def trans_in_name(self, value):
        self._trans_in_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.trans_in_account:
            if hasattr(self.trans_in_account, 'to_alipay_dict'):
                params['trans_in_account'] = self.trans_in_account.to_alipay_dict()
            else:
                params['trans_in_account'] = self.trans_in_account
        if self.trans_in_name:
            if hasattr(self.trans_in_name, 'to_alipay_dict'):
                params['trans_in_name'] = self.trans_in_name.to_alipay_dict()
            else:
                params['trans_in_name'] = self.trans_in_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantSettleRelationProcessorRequest()
        if 'rate' in d:
            o.rate = d['rate']
        if 'trans_in_account' in d:
            o.trans_in_account = d['trans_in_account']
        if 'trans_in_name' in d:
            o.trans_in_name = d['trans_in_name']
        return o


