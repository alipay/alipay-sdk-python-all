#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommonBillQueryModel(object):

    def __init__(self):
        self._bill_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommonBillQueryModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        return o


