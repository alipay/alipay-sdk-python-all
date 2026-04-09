#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FindTextRequest import FindTextRequest


class AnttechOceanbaseObglobalBailingualBatchqueryModel(object):

    def __init__(self):
        self._find_text_request = None

    @property
    def find_text_request(self):
        return self._find_text_request

    @find_text_request.setter
    def find_text_request(self, value):
        if isinstance(value, FindTextRequest):
            self._find_text_request = value
        else:
            self._find_text_request = FindTextRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.find_text_request:
            if hasattr(self.find_text_request, 'to_alipay_dict'):
                params['find_text_request'] = self.find_text_request.to_alipay_dict()
            else:
                params['find_text_request'] = self.find_text_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalBailingualBatchqueryModel()
        if 'find_text_request' in d:
            o.find_text_request = d['find_text_request']
        return o


