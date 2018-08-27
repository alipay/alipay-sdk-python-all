#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Condition import Condition


class KoubeiMarketingCampaignActivityBatchqueryModel(object):

    def __init__(self):
        self._operator_id = None
        self._operator_type = None
        self._page_number = None
        self._page_size = None
        self._query_criterias = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def query_criterias(self):
        return self._query_criterias

    @query_criterias.setter
    def query_criterias(self, value):
        if isinstance(value, list):
            self._query_criterias = list()
            for i in value:
                if isinstance(i, Condition):
                    self._query_criterias.append(i)
                else:
                    self._query_criterias.append(Condition.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.query_criterias:
            if isinstance(self.query_criterias, list):
                for i in range(0, len(self.query_criterias)):
                    element = self.query_criterias[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_criterias[i] = element.to_alipay_dict()
            if hasattr(self.query_criterias, 'to_alipay_dict'):
                params['query_criterias'] = self.query_criterias.to_alipay_dict()
            else:
                params['query_criterias'] = self.query_criterias
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignActivityBatchqueryModel()
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_criterias' in d:
            o.query_criterias = d['query_criterias']
        return o


