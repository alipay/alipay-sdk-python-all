#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvBillQueryModel(object):

    def __init__(self):
        self._product_code = None
        self._query_date = None
        self._supervisor_id_number = None
        self._task_id = None

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
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
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvBillQueryModel()
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'query_date' in d:
            o.query_date = d['query_date']
        if 'supervisor_id_number' in d:
            o.supervisor_id_number = d['supervisor_id_number']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


