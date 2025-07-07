#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityTestmysqltoobQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityTestmysqltoobQueryResponse, self).__init__()
        self._test_02 = None

    @property
    def test_02(self):
        return self._test_02

    @test_02.setter
    def test_02(self, value):
        if isinstance(value, list):
            self._test_02 = list()
            for i in value:
                self._test_02.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityTestmysqltoobQueryResponse, self).parse_response_content(response_content)
        if 'test_02' in response:
            self.test_02 = response['test_02']
