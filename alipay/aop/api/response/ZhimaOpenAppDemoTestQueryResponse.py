#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaOpenAppDemoTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaOpenAppDemoTestQueryResponse, self).__init__()
        self._platform_a = None
        self._test_2 = None
        self._test_6 = None
        self._test_id = None
        self._test_id_open_id = None
        self._test_number = None

    @property
    def platform_a(self):
        return self._platform_a

    @platform_a.setter
    def platform_a(self, value):
        self._platform_a = value
    @property
    def test_2(self):
        return self._test_2

    @test_2.setter
    def test_2(self, value):
        self._test_2 = value
    @property
    def test_6(self):
        return self._test_6

    @test_6.setter
    def test_6(self, value):
        self._test_6 = value
    @property
    def test_id(self):
        return self._test_id

    @test_id.setter
    def test_id(self, value):
        self._test_id = value
    @property
    def test_id_open_id(self):
        return self._test_id_open_id

    @test_id_open_id.setter
    def test_id_open_id(self, value):
        self._test_id_open_id = value
    @property
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        self._test_number = value

    def parse_response_content(self, response_content):
        response = super(ZhimaOpenAppDemoTestQueryResponse, self).parse_response_content(response_content)
        if 'platform_a' in response:
            self.platform_a = response['platform_a']
        if 'test_2' in response:
            self.test_2 = response['test_2']
        if 'test_6' in response:
            self.test_6 = response['test_6']
        if 'test_id' in response:
            self.test_id = response['test_id']
        if 'test_id_open_id' in response:
            self.test_id_open_id = response['test_id_open_id']
        if 'test_number' in response:
            self.test_number = response['test_number']
