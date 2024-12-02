#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryCriteria import QueryCriteria


class AlipayCloudCloudpromoMessageDeliveryQueryModel(object):

    def __init__(self):
        self._query_criteria = None
        self._record_id = None

    @property
    def query_criteria(self):
        return self._query_criteria

    @query_criteria.setter
    def query_criteria(self, value):
        if isinstance(value, QueryCriteria):
            self._query_criteria = value
        else:
            self._query_criteria = QueryCriteria.from_alipay_dict(value)
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_criteria:
            if hasattr(self.query_criteria, 'to_alipay_dict'):
                params['query_criteria'] = self.query_criteria.to_alipay_dict()
            else:
                params['query_criteria'] = self.query_criteria
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMessageDeliveryQueryModel()
        if 'query_criteria' in d:
            o.query_criteria = d['query_criteria']
        if 'record_id' in d:
            o.record_id = d['record_id']
        return o


