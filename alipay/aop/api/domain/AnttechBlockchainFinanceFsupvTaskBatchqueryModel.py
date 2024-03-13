#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvTaskBatchqueryModel(object):

    def __init__(self):
        self._fund_supv_product_code = None
        self._query_date = None
        self._supervisor_id_number = None

    @property
    def fund_supv_product_code(self):
        return self._fund_supv_product_code

    @fund_supv_product_code.setter
    def fund_supv_product_code(self, value):
        self._fund_supv_product_code = value
    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value
    @property
    def supervisor_id_number(self):
        return self._supervisor_id_number

    @supervisor_id_number.setter
    def supervisor_id_number(self, value):
        self._supervisor_id_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_product_code:
            if hasattr(self.fund_supv_product_code, 'to_alipay_dict'):
                params['fund_supv_product_code'] = self.fund_supv_product_code.to_alipay_dict()
            else:
                params['fund_supv_product_code'] = self.fund_supv_product_code
        if self.query_date:
            if hasattr(self.query_date, 'to_alipay_dict'):
                params['query_date'] = self.query_date.to_alipay_dict()
            else:
                params['query_date'] = self.query_date
        if self.supervisor_id_number:
            if hasattr(self.supervisor_id_number, 'to_alipay_dict'):
                params['supervisor_id_number'] = self.supervisor_id_number.to_alipay_dict()
            else:
                params['supervisor_id_number'] = self.supervisor_id_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvTaskBatchqueryModel()
        if 'fund_supv_product_code' in d:
            o.fund_supv_product_code = d['fund_supv_product_code']
        if 'query_date' in d:
            o.query_date = d['query_date']
        if 'supervisor_id_number' in d:
            o.supervisor_id_number = d['supervisor_id_number']
        return o


