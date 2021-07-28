#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperatorQuery import OperatorQuery


class AlipayOpenAuthOperatorInfoQueryModel(object):

    def __init__(self):
        self._operator_query = None
        self._tenant_id = None

    @property
    def operator_query(self):
        return self._operator_query

    @operator_query.setter
    def operator_query(self, value):
        if isinstance(value, OperatorQuery):
            self._operator_query = value
        else:
            self._operator_query = OperatorQuery.from_alipay_dict(value)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_query:
            if hasattr(self.operator_query, 'to_alipay_dict'):
                params['operator_query'] = self.operator_query.to_alipay_dict()
            else:
                params['operator_query'] = self.operator_query
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
        o = AlipayOpenAuthOperatorInfoQueryModel()
        if 'operator_query' in d:
            o.operator_query = d['operator_query']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


