#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntProdpaasArrangementRebateRateQueryModel(object):

    def __init__(self):
        self._data_item_name = None
        self._first_category_id = None
        self._gmt_query = None

    @property
    def data_item_name(self):
        return self._data_item_name

    @data_item_name.setter
    def data_item_name(self, value):
        self._data_item_name = value
    @property
    def first_category_id(self):
        return self._first_category_id

    @first_category_id.setter
    def first_category_id(self, value):
        self._first_category_id = value
    @property
    def gmt_query(self):
        return self._gmt_query

    @gmt_query.setter
    def gmt_query(self, value):
        self._gmt_query = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_item_name:
            if hasattr(self.data_item_name, 'to_alipay_dict'):
                params['data_item_name'] = self.data_item_name.to_alipay_dict()
            else:
                params['data_item_name'] = self.data_item_name
        if self.first_category_id:
            if hasattr(self.first_category_id, 'to_alipay_dict'):
                params['first_category_id'] = self.first_category_id.to_alipay_dict()
            else:
                params['first_category_id'] = self.first_category_id
        if self.gmt_query:
            if hasattr(self.gmt_query, 'to_alipay_dict'):
                params['gmt_query'] = self.gmt_query.to_alipay_dict()
            else:
                params['gmt_query'] = self.gmt_query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntProdpaasArrangementRebateRateQueryModel()
        if 'data_item_name' in d:
            o.data_item_name = d['data_item_name']
        if 'first_category_id' in d:
            o.first_category_id = d['first_category_id']
        if 'gmt_query' in d:
            o.gmt_query = d['gmt_query']
        return o


