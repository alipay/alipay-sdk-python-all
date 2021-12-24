#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyMerchantSignQueryModel(object):

    def __init__(self):
        self._out_request_no = None
        self._process_no = None
        self._wallet_id = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def process_no(self):
        return self._process_no

    @process_no.setter
    def process_no(self, value):
        self._process_no = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.process_no:
            if hasattr(self.process_no, 'to_alipay_dict'):
                params['process_no'] = self.process_no.to_alipay_dict()
            else:
                params['process_no'] = self.process_no
        if self.wallet_id:
            if hasattr(self.wallet_id, 'to_alipay_dict'):
                params['wallet_id'] = self.wallet_id.to_alipay_dict()
            else:
                params['wallet_id'] = self.wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyMerchantSignQueryModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'process_no' in d:
            o.process_no = d['process_no']
        if 'wallet_id' in d:
            o.wallet_id = d['wallet_id']
        return o


