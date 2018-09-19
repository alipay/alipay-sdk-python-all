#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReduceToAmtDstCampPrizeModel(object):

    def __init__(self):
        self._reduct_to_amt = None

    @property
    def reduct_to_amt(self):
        return self._reduct_to_amt

    @reduct_to_amt.setter
    def reduct_to_amt(self, value):
        self._reduct_to_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.reduct_to_amt:
            if hasattr(self.reduct_to_amt, 'to_alipay_dict'):
                params['reduct_to_amt'] = self.reduct_to_amt.to_alipay_dict()
            else:
                params['reduct_to_amt'] = self.reduct_to_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReduceToAmtDstCampPrizeModel()
        if 'reduct_to_amt' in d:
            o.reduct_to_amt = d['reduct_to_amt']
        return o


