#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicAuditQueryReq import ScenicAuditQueryReq


class AlipayCommerceDataScenicMappingQueryModel(object):

    def __init__(self):
        self._scenic_audit_query_req = None

    @property
    def scenic_audit_query_req(self):
        return self._scenic_audit_query_req

    @scenic_audit_query_req.setter
    def scenic_audit_query_req(self, value):
        if isinstance(value, list):
            self._scenic_audit_query_req = list()
            for i in value:
                if isinstance(i, ScenicAuditQueryReq):
                    self._scenic_audit_query_req.append(i)
                else:
                    self._scenic_audit_query_req.append(ScenicAuditQueryReq.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scenic_audit_query_req:
            if isinstance(self.scenic_audit_query_req, list):
                for i in range(0, len(self.scenic_audit_query_req)):
                    element = self.scenic_audit_query_req[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scenic_audit_query_req[i] = element.to_alipay_dict()
            if hasattr(self.scenic_audit_query_req, 'to_alipay_dict'):
                params['scenic_audit_query_req'] = self.scenic_audit_query_req.to_alipay_dict()
            else:
                params['scenic_audit_query_req'] = self.scenic_audit_query_req
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataScenicMappingQueryModel()
        if 'scenic_audit_query_req' in d:
            o.scenic_audit_query_req = d['scenic_audit_query_req']
        return o


