#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GovDocRequest(object):

    def __init__(self):
        self._gov_doc_request = None
        self._test = None

    @property
    def gov_doc_request(self):
        return self._gov_doc_request

    @gov_doc_request.setter
    def gov_doc_request(self, value):
        self._gov_doc_request = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value


    def to_alipay_dict(self):
        params = dict()
        if self.gov_doc_request:
            if hasattr(self.gov_doc_request, 'to_alipay_dict'):
                params['gov_doc_request'] = self.gov_doc_request.to_alipay_dict()
            else:
                params['gov_doc_request'] = self.gov_doc_request
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GovDocRequest()
        if 'gov_doc_request' in d:
            o.gov_doc_request = d['gov_doc_request']
        if 'test' in d:
            o.test = d['test']
        return o


