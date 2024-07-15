#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolutionBatchQueryModel(object):

    def __init__(self):
        self._batch_no = None
        self._out_batch_no = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.out_batch_no:
            if hasattr(self.out_batch_no, 'to_alipay_dict'):
                params['out_batch_no'] = self.out_batch_no.to_alipay_dict()
            else:
                params['out_batch_no'] = self.out_batch_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolutionBatchQueryModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'out_batch_no' in d:
            o.out_batch_no = d['out_batch_no']
        return o


