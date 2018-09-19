#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeContractBatchinfoQueryModel(object):

    def __init__(self):
        self._activity_name = None
        self._batch_index = None
        self._category = None
        self._query_date = None
        self._transaction_id = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def batch_index(self):
        return self._batch_index

    @batch_index.setter
    def batch_index(self, value):
        self._batch_index = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.batch_index:
            if hasattr(self.batch_index, 'to_alipay_dict'):
                params['batch_index'] = self.batch_index.to_alipay_dict()
            else:
                params['batch_index'] = self.batch_index
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.query_date:
            if hasattr(self.query_date, 'to_alipay_dict'):
                params['query_date'] = self.query_date.to_alipay_dict()
            else:
                params['query_date'] = self.query_date
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeContractBatchinfoQueryModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'batch_index' in d:
            o.batch_index = d['batch_index']
        if 'category' in d:
            o.category = d['category']
        if 'query_date' in d:
            o.query_date = d['query_date']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


