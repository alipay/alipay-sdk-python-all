#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsDataAutodamageEstimateQueryModel(object):

    def __init__(self):
        self._estimate_no = None

    @property
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.estimate_no:
            if hasattr(self.estimate_no, 'to_alipay_dict'):
                params['estimate_no'] = self.estimate_no.to_alipay_dict()
            else:
                params['estimate_no'] = self.estimate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAutodamageEstimateQueryModel()
        if 'estimate_no' in d:
            o.estimate_no = d['estimate_no']
        return o


