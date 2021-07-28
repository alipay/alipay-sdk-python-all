#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundBatchAppPayModel(object):

    def __init__(self):
        self._batch_trans_id = None

    @property
    def batch_trans_id(self):
        return self._batch_trans_id

    @batch_trans_id.setter
    def batch_trans_id(self, value):
        self._batch_trans_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_trans_id:
            if hasattr(self.batch_trans_id, 'to_alipay_dict'):
                params['batch_trans_id'] = self.batch_trans_id.to_alipay_dict()
            else:
                params['batch_trans_id'] = self.batch_trans_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBatchAppPayModel()
        if 'batch_trans_id' in d:
            o.batch_trans_id = d['batch_trans_id']
        return o


