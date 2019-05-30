#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeBatchSettleQueryModel(object):

    def __init__(self):
        self._extend_params = None
        self._out_request_no = None
        self._settle_no = None

    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.settle_no:
            if hasattr(self.settle_no, 'to_alipay_dict'):
                params['settle_no'] = self.settle_no.to_alipay_dict()
            else:
                params['settle_no'] = self.settle_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBatchSettleQueryModel()
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'settle_no' in d:
            o.settle_no = d['settle_no']
        return o


