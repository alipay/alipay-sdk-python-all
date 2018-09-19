#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbPosBillDishDetail(object):

    def __init__(self):
        self._out_detail_no = None
        self._trans_amount = None

    @property
    def out_detail_no(self):
        return self._out_detail_no

    @out_detail_no.setter
    def out_detail_no(self, value):
        self._out_detail_no = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_detail_no:
            if hasattr(self.out_detail_no, 'to_alipay_dict'):
                params['out_detail_no'] = self.out_detail_no.to_alipay_dict()
            else:
                params['out_detail_no'] = self.out_detail_no
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbPosBillDishDetail()
        if 'out_detail_no' in d:
            o.out_detail_no = d['out_detail_no']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        return o


