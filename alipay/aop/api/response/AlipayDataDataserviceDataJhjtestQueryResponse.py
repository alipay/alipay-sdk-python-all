#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceDataJhjtestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDataJhjtestQueryResponse, self).__init__()
        self._test_out_other = None
        self._test_out_string = None
        self._test_out_string_yincang = None

    @property
    def test_out_other(self):
        return self._test_out_other

    @test_out_other.setter
    def test_out_other(self, value):
        self._test_out_other = value
    @property
    def test_out_string(self):
        return self._test_out_string

    @test_out_string.setter
    def test_out_string(self, value):
        self._test_out_string = value
    @property
    def test_out_string_yincang(self):
        return self._test_out_string_yincang

    @test_out_string_yincang.setter
    def test_out_string_yincang(self, value):
        self._test_out_string_yincang = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDataJhjtestQueryResponse, self).parse_response_content(response_content)
        if 'test_out_other' in response:
            self.test_out_other = response['test_out_other']
        if 'test_out_string' in response:
            self.test_out_string = response['test_out_string']
        if 'test_out_string_yincang' in response:
            self.test_out_string_yincang = response['test_out_string_yincang']
