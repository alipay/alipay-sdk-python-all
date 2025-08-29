#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoKnowledgeDocumentUnbindModel(object):

    def __init__(self):
        self._api_key = None
        self._customer_id = None
        self._document_id = None
        self._knowledge_base_id = None
        self._operator = None
        self._tenant_id = None

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
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        self._document_id = value
    @property
    def knowledge_base_id(self):
        return self._knowledge_base_id

    @knowledge_base_id.setter
    def knowledge_base_id(self, value):
        self._knowledge_base_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


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
        if self.document_id:
            if hasattr(self.document_id, 'to_alipay_dict'):
                params['document_id'] = self.document_id.to_alipay_dict()
            else:
                params['document_id'] = self.document_id
        if self.knowledge_base_id:
            if hasattr(self.knowledge_base_id, 'to_alipay_dict'):
                params['knowledge_base_id'] = self.knowledge_base_id.to_alipay_dict()
            else:
                params['knowledge_base_id'] = self.knowledge_base_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoKnowledgeDocumentUnbindModel()
        if 'api_key' in d:
            o.api_key = d['api_key']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'document_id' in d:
            o.document_id = d['document_id']
        if 'knowledge_base_id' in d:
            o.knowledge_base_id = d['knowledge_base_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


