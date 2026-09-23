#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyFundRepaymentQueryModel(object):

    def __init__(self):
        self._out_request_from = None
        self._out_request_no = None
        self._payer_wallet_id = None

    @property
    def out_request_from(self):
        return self._out_request_from

    @out_request_from.setter
    def out_request_from(self, value):
        self._out_request_from = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def payer_wallet_id(self):
        return self._payer_wallet_id

    @payer_wallet_id.setter
    def payer_wallet_id(self, value):
        self._payer_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_from:
            if hasattr(self.out_request_from, 'to_alipay_dict'):
                params['out_request_from'] = self.out_request_from.to_alipay_dict()
            else:
                params['out_request_from'] = self.out_request_from
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.payer_wallet_id:
            if hasattr(self.payer_wallet_id, 'to_alipay_dict'):
                params['payer_wallet_id'] = self.payer_wallet_id.to_alipay_dict()
            else:
                params['payer_wallet_id'] = self.payer_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyFundRepaymentQueryModel()
        if 'out_request_from' in d:
            o.out_request_from = d['out_request_from']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'payer_wallet_id' in d:
            o.payer_wallet_id = d['payer_wallet_id']
        return o


