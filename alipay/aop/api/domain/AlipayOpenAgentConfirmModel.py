#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentConfirmModel(object):

    def __init__(self):
        self._batch_no = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentConfirmModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        return o


