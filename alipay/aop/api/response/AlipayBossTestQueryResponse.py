#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossTestQueryResponse, self).__init__()
        self._test_01 = None

    @property
    def test_01(self):
        return self._test_01

    @test_01.setter
    def test_01(self, value):
        self._test_01 = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossTestQueryResponse, self).parse_response_content(response_content)
        if 'test_01' in response:
            self.test_01 = response['test_01']
