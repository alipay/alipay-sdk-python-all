#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OuCodeQueryRequest import OuCodeQueryRequest


class AnttechOceanbaseOudefinitionCodeQueryModel(object):

    def __init__(self):
        self._ou_code_query_request = None

    @property
    def ou_code_query_request(self):
        return self._ou_code_query_request

    @ou_code_query_request.setter
    def ou_code_query_request(self, value):
        if isinstance(value, OuCodeQueryRequest):
            self._ou_code_query_request = value
        else:
            self._ou_code_query_request = OuCodeQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ou_code_query_request:
            if hasattr(self.ou_code_query_request, 'to_alipay_dict'):
                params['ou_code_query_request'] = self.ou_code_query_request.to_alipay_dict()
            else:
                params['ou_code_query_request'] = self.ou_code_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseOudefinitionCodeQueryModel()
        if 'ou_code_query_request' in d:
            o.ou_code_query_request = d['ou_code_query_request']
        return o


