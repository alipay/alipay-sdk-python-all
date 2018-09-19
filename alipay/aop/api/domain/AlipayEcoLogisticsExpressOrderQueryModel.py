#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoLogisticsExpressOrderQueryModel(object):

    def __init__(self):
        self._logis_merch_code = None
        self._order_no = None

    @property
    def logis_merch_code(self):
        return self._logis_merch_code

    @logis_merch_code.setter
    def logis_merch_code(self, value):
        self._logis_merch_code = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logis_merch_code:
            if hasattr(self.logis_merch_code, 'to_alipay_dict'):
                params['logis_merch_code'] = self.logis_merch_code.to_alipay_dict()
            else:
                params['logis_merch_code'] = self.logis_merch_code
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoLogisticsExpressOrderQueryModel()
        if 'logis_merch_code' in d:
            o.logis_merch_code = d['logis_merch_code']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


