#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalExaminationCategorylistQueryModel(object):

    def __init__(self):
        self._category_id = None
        self._category_state = None
        self._category_type = None
        self._query_type = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_state(self):
        return self._category_state

    @category_state.setter
    def category_state(self, value):
        self._category_state = value
    @property
    def category_type(self):
        return self._category_type

    @category_type.setter
    def category_type(self, value):
        self._category_type = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_state:
            if hasattr(self.category_state, 'to_alipay_dict'):
                params['category_state'] = self.category_state.to_alipay_dict()
            else:
                params['category_state'] = self.category_state
        if self.category_type:
            if hasattr(self.category_type, 'to_alipay_dict'):
                params['category_type'] = self.category_type.to_alipay_dict()
            else:
                params['category_type'] = self.category_type
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalExaminationCategorylistQueryModel()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_state' in d:
            o.category_state = d['category_state']
        if 'category_type' in d:
            o.category_type = d['category_type']
        if 'query_type' in d:
            o.query_type = d['query_type']
        return o


