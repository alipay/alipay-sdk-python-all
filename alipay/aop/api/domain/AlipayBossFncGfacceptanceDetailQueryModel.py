#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIQueryRequest import GFAOpenAPIQueryRequest


class AlipayBossFncGfacceptanceDetailQueryModel(object):

    def __init__(self):
        self._principal_id = None
        self._query = None

    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        if isinstance(value, GFAOpenAPIQueryRequest):
            self._query = value
        else:
            self._query = GFAOpenAPIQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfacceptanceDetailQueryModel()
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'query' in d:
            o.query = d['query']
        return o


