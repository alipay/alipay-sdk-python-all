#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniappsaftyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniappsaftyQueryResponse, self).__init__()
        self._intercept_cnt = None
        self._intercept_ratio = None
        self._intercept_trend = None
        self._request_cnt = None

    @property
    def intercept_cnt(self):
        return self._intercept_cnt

    @intercept_cnt.setter
    def intercept_cnt(self, value):
        self._intercept_cnt = value
    @property
    def intercept_ratio(self):
        return self._intercept_ratio

    @intercept_ratio.setter
    def intercept_ratio(self, value):
        self._intercept_ratio = value
    @property
    def intercept_trend(self):
        return self._intercept_trend

    @intercept_trend.setter
    def intercept_trend(self, value):
        self._intercept_trend = value
    @property
    def request_cnt(self):
        return self._request_cnt

    @request_cnt.setter
    def request_cnt(self, value):
        self._request_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniappsaftyQueryResponse, self).parse_response_content(response_content)
        if 'intercept_cnt' in response:
            self.intercept_cnt = response['intercept_cnt']
        if 'intercept_ratio' in response:
            self.intercept_ratio = response['intercept_ratio']
        if 'intercept_trend' in response:
            self.intercept_trend = response['intercept_trend']
        if 'request_cnt' in response:
            self.request_cnt = response['request_cnt']
