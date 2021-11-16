#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncAggregationDetailQueryModel(object):

    def __init__(self):
        self._po_no = None

    @property
    def po_no(self):
        return self._po_no

    @po_no.setter
    def po_no(self, value):
        self._po_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.po_no:
            if hasattr(self.po_no, 'to_alipay_dict'):
                params['po_no'] = self.po_no.to_alipay_dict()
            else:
                params['po_no'] = self.po_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncAggregationDetailQueryModel()
        if 'po_no' in d:
            o.po_no = d['po_no']
        return o


