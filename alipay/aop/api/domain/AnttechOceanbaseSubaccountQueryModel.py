#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountQueryRequest import SubAccountQueryRequest


class AnttechOceanbaseSubaccountQueryModel(object):

    def __init__(self):
        self._sub_account_query_request = None

    @property
    def sub_account_query_request(self):
        return self._sub_account_query_request

    @sub_account_query_request.setter
    def sub_account_query_request(self, value):
        if isinstance(value, SubAccountQueryRequest):
            self._sub_account_query_request = value
        else:
            self._sub_account_query_request = SubAccountQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sub_account_query_request:
            if hasattr(self.sub_account_query_request, 'to_alipay_dict'):
                params['sub_account_query_request'] = self.sub_account_query_request.to_alipay_dict()
            else:
                params['sub_account_query_request'] = self.sub_account_query_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseSubaccountQueryModel()
        if 'sub_account_query_request' in d:
            o.sub_account_query_request = d['sub_account_query_request']
        return o


