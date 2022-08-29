#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Marketingtest import Marketingtest


class AlipayMarketingXuanyitestTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingXuanyitestTransferResponse, self).__init__()
        self._test = None
        self._test_21 = None

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, list):
            self._test = list()
            for i in value:
                self._test.append(i)
    @property
    def test_21(self):
        return self._test_21

    @test_21.setter
    def test_21(self, value):
        if isinstance(value, list):
            self._test_21 = list()
            for i in value:
                if isinstance(i, Marketingtest):
                    self._test_21.append(i)
                else:
                    self._test_21.append(Marketingtest.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingXuanyitestTransferResponse, self).parse_response_content(response_content)
        if 'test' in response:
            self.test = response['test']
        if 'test_21' in response:
            self.test_21 = response['test_21']
