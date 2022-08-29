#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcsmartCommonAppInfo import RcsmartCommonAppInfo
from alipay.aop.api.domain.ApprovalQuery import ApprovalQuery


class AlipayFincoreComplianceRcservcenterRcsmartQueryModel(object):

    def __init__(self):
        self._app_info = None
        self._approval_query = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        if isinstance(value, RcsmartCommonAppInfo):
            self._app_info = value
        else:
            self._app_info = RcsmartCommonAppInfo.from_alipay_dict(value)
    @property
    def approval_query(self):
        return self._approval_query

    @approval_query.setter
    def approval_query(self, value):
        if isinstance(value, ApprovalQuery):
            self._approval_query = value
        else:
            self._approval_query = ApprovalQuery.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.approval_query:
            if hasattr(self.approval_query, 'to_alipay_dict'):
                params['approval_query'] = self.approval_query.to_alipay_dict()
            else:
                params['approval_query'] = self.approval_query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcservcenterRcsmartQueryModel()
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'approval_query' in d:
            o.approval_query = d['approval_query']
        return o


