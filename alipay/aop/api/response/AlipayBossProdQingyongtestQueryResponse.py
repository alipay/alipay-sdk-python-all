#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdQingyongtestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdQingyongtestQueryResponse, self).__init__()
        self._is_success = None
        self._test_chucan = None

    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def test_chucan(self):
        return self._test_chucan

    @test_chucan.setter
    def test_chucan(self, value):
        self._test_chucan = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdQingyongtestQueryResponse, self).parse_response_content(response_content)
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'test_chucan' in response:
            self.test_chucan = response['test_chucan']
