#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrgRoleQuery import OrgRoleQuery
from alipay.aop.api.domain.QueryInfo import QueryInfo


class AlipayBossBaseAntauthorizeOrgroleQueryModel(object):

    def __init__(self):
        self._query = None
        self._query_info = None

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        if isinstance(value, OrgRoleQuery):
            self._query = value
        else:
            self._query = OrgRoleQuery.from_alipay_dict(value)
    @property
    def query_info(self):
        return self._query_info

    @query_info.setter
    def query_info(self, value):
        if isinstance(value, QueryInfo):
            self._query_info = value
        else:
            self._query_info = QueryInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.query_info:
            if hasattr(self.query_info, 'to_alipay_dict'):
                params['query_info'] = self.query_info.to_alipay_dict()
            else:
                params['query_info'] = self.query_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseAntauthorizeOrgroleQueryModel()
        if 'query' in d:
            o.query = d['query']
        if 'query_info' in d:
            o.query_info = d['query_info']
        return o


