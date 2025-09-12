#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KnowledgeBaseSearchOption import KnowledgeBaseSearchOption


class AlipayCloudCloudpromoKnowledgeRagGenerateModel(object):

    def __init__(self):
        self._api_key = None
        self._customer_id = None
        self._options = None
        self._query = None
        self._similarity_threshold = None
        self._tenant_id = None
        self._top_k = None

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, KnowledgeBaseSearchOption):
                    self._options.append(i)
                else:
                    self._options.append(KnowledgeBaseSearchOption.from_alipay_dict(i))
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def similarity_threshold(self):
        return self._similarity_threshold

    @similarity_threshold.setter
    def similarity_threshold(self, value):
        self._similarity_threshold = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def top_k(self):
        return self._top_k

    @top_k.setter
    def top_k(self, value):
        self._top_k = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_key:
            if hasattr(self.api_key, 'to_alipay_dict'):
                params['api_key'] = self.api_key.to_alipay_dict()
            else:
                params['api_key'] = self.api_key
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.similarity_threshold:
            if hasattr(self.similarity_threshold, 'to_alipay_dict'):
                params['similarity_threshold'] = self.similarity_threshold.to_alipay_dict()
            else:
                params['similarity_threshold'] = self.similarity_threshold
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.top_k:
            if hasattr(self.top_k, 'to_alipay_dict'):
                params['top_k'] = self.top_k.to_alipay_dict()
            else:
                params['top_k'] = self.top_k
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoKnowledgeRagGenerateModel()
        if 'api_key' in d:
            o.api_key = d['api_key']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'options' in d:
            o.options = d['options']
        if 'query' in d:
            o.query = d['query']
        if 'similarity_threshold' in d:
            o.similarity_threshold = d['similarity_threshold']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'top_k' in d:
            o.top_k = d['top_k']
        return o


