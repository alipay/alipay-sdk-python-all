#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryData import QueryData


class AlipayCommerceMedicalFulfillmentListQueryModel(object):

    def __init__(self):
        self._query_data = None

    @property
    def query_data(self):
        return self._query_data

    @query_data.setter
    def query_data(self, value):
        if isinstance(value, list):
            self._query_data = list()
            for i in value:
                if isinstance(i, QueryData):
                    self._query_data.append(i)
                else:
                    self._query_data.append(QueryData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.query_data:
            if isinstance(self.query_data, list):
                for i in range(0, len(self.query_data)):
                    element = self.query_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_data[i] = element.to_alipay_dict()
            if hasattr(self.query_data, 'to_alipay_dict'):
                params['query_data'] = self.query_data.to_alipay_dict()
            else:
                params['query_data'] = self.query_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFulfillmentListQueryModel()
        if 'query_data' in d:
            o.query_data = d['query_data']
        return o


