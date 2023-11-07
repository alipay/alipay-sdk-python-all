#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ListCallDetailRecordsRequest import ListCallDetailRecordsRequest


class AnttechOceanbaseObglobalListcalldetailsBatchqueryModel(object):

    def __init__(self):
        self._list_call_detail_records_request = None

    @property
    def list_call_detail_records_request(self):
        return self._list_call_detail_records_request

    @list_call_detail_records_request.setter
    def list_call_detail_records_request(self, value):
        if isinstance(value, ListCallDetailRecordsRequest):
            self._list_call_detail_records_request = value
        else:
            self._list_call_detail_records_request = ListCallDetailRecordsRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.list_call_detail_records_request:
            if hasattr(self.list_call_detail_records_request, 'to_alipay_dict'):
                params['list_call_detail_records_request'] = self.list_call_detail_records_request.to_alipay_dict()
            else:
                params['list_call_detail_records_request'] = self.list_call_detail_records_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalListcalldetailsBatchqueryModel()
        if 'list_call_detail_records_request' in d:
            o.list_call_detail_records_request = d['list_call_detail_records_request']
        return o


