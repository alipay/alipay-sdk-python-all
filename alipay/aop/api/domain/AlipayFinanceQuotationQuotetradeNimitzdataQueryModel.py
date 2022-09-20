#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DatasetRequest import DatasetRequest


class AlipayFinanceQuotationQuotetradeNimitzdataQueryModel(object):

    def __init__(self):
        self._dataset_request = None
        self._request_id = None

    @property
    def dataset_request(self):
        return self._dataset_request

    @dataset_request.setter
    def dataset_request(self, value):
        if isinstance(value, DatasetRequest):
            self._dataset_request = value
        else:
            self._dataset_request = DatasetRequest.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dataset_request:
            if hasattr(self.dataset_request, 'to_alipay_dict'):
                params['dataset_request'] = self.dataset_request.to_alipay_dict()
            else:
                params['dataset_request'] = self.dataset_request
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeNimitzdataQueryModel()
        if 'dataset_request' in d:
            o.dataset_request = d['dataset_request']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


