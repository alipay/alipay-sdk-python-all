#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantSettleRelationProcessorResponse(object):

    def __init__(self):
        self._rate = None
        self._trans_in_account = None
        self._trans_in_id = None
        self._trans_in_name = None
        self._trans_in_type = None
        self._trans_out_account = None
        self._trans_out_id = None

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
    def trans_in_id(self):
        return self._trans_in_id

    @trans_in_id.setter
    def trans_in_id(self, value):
        self._trans_in_id = value
    @property
    def trans_in_name(self):
        return self._trans_in_name

    @trans_in_name.setter
    def trans_in_name(self, value):
        self._trans_in_name = value
    @property
    def trans_in_type(self):
        return self._trans_in_type

    @trans_in_type.setter
    def trans_in_type(self, value):
        self._trans_in_type = value
    @property
    def trans_out_account(self):
        return self._trans_out_account

    @trans_out_account.setter
    def trans_out_account(self, value):
        self._trans_out_account = value
    @property
    def trans_out_id(self):
        return self._trans_out_id

    @trans_out_id.setter
    def trans_out_id(self, value):
        self._trans_out_id = value


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
        if self.trans_in_id:
            if hasattr(self.trans_in_id, 'to_alipay_dict'):
                params['trans_in_id'] = self.trans_in_id.to_alipay_dict()
            else:
                params['trans_in_id'] = self.trans_in_id
        if self.trans_in_name:
            if hasattr(self.trans_in_name, 'to_alipay_dict'):
                params['trans_in_name'] = self.trans_in_name.to_alipay_dict()
            else:
                params['trans_in_name'] = self.trans_in_name
        if self.trans_in_type:
            if hasattr(self.trans_in_type, 'to_alipay_dict'):
                params['trans_in_type'] = self.trans_in_type.to_alipay_dict()
            else:
                params['trans_in_type'] = self.trans_in_type
        if self.trans_out_account:
            if hasattr(self.trans_out_account, 'to_alipay_dict'):
                params['trans_out_account'] = self.trans_out_account.to_alipay_dict()
            else:
                params['trans_out_account'] = self.trans_out_account
        if self.trans_out_id:
            if hasattr(self.trans_out_id, 'to_alipay_dict'):
                params['trans_out_id'] = self.trans_out_id.to_alipay_dict()
            else:
                params['trans_out_id'] = self.trans_out_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantSettleRelationProcessorResponse()
        if 'rate' in d:
            o.rate = d['rate']
        if 'trans_in_account' in d:
            o.trans_in_account = d['trans_in_account']
        if 'trans_in_id' in d:
            o.trans_in_id = d['trans_in_id']
        if 'trans_in_name' in d:
            o.trans_in_name = d['trans_in_name']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        if 'trans_out_account' in d:
            o.trans_out_account = d['trans_out_account']
        if 'trans_out_id' in d:
            o.trans_out_id = d['trans_out_id']
        return o


