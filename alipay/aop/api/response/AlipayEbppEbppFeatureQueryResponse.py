#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppEbppFeatureQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEbppFeatureQueryResponse, self).__init__()
        self._batch_id = None
        self._cnt = None
        self._feature_ext = None
        self._session_end = None
        self._session_start = None
        self._sum_amt = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def cnt(self):
        return self._cnt

    @cnt.setter
    def cnt(self, value):
        self._cnt = value
    @property
    def feature_ext(self):
        return self._feature_ext

    @feature_ext.setter
    def feature_ext(self, value):
        self._feature_ext = value
    @property
    def session_end(self):
        return self._session_end

    @session_end.setter
    def session_end(self, value):
        self._session_end = value
    @property
    def session_start(self):
        return self._session_start

    @session_start.setter
    def session_start(self, value):
        self._session_start = value
    @property
    def sum_amt(self):
        return self._sum_amt

    @sum_amt.setter
    def sum_amt(self, value):
        self._sum_amt = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppEbppFeatureQueryResponse, self).parse_response_content(response_content)
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
        if 'cnt' in response:
            self.cnt = response['cnt']
        if 'feature_ext' in response:
            self.feature_ext = response['feature_ext']
        if 'session_end' in response:
            self.session_end = response['session_end']
        if 'session_start' in response:
            self.session_start = response['session_start']
        if 'sum_amt' in response:
            self.sum_amt = response['sum_amt']
