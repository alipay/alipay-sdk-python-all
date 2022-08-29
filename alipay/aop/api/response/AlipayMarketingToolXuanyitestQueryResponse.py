#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingToolXuanyitestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolXuanyitestQueryResponse, self).__init__()
        self._test_100 = None
        self._test_101 = None

    @property
    def test_100(self):
        return self._test_100

    @test_100.setter
    def test_100(self, value):
        self._test_100 = value
    @property
    def test_101(self):
        return self._test_101

    @test_101.setter
    def test_101(self, value):
        self._test_101 = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolXuanyitestQueryResponse, self).parse_response_content(response_content)
        if 'test_100' in response:
            self.test_100 = response['test_100']
        if 'test_101' in response:
            self.test_101 = response['test_101']
