#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppOpenbizmockDesensitiveQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenbizmockDesensitiveQueryResponse, self).__init__()
        self._test_field_converter = None
        self._test_fields_converter = None

    @property
    def test_field_converter(self):
        return self._test_field_converter

    @test_field_converter.setter
    def test_field_converter(self, value):
        self._test_field_converter = value
    @property
    def test_fields_converter(self):
        return self._test_fields_converter

    @test_fields_converter.setter
    def test_fields_converter(self, value):
        if isinstance(value, list):
            self._test_fields_converter = list()
            for i in value:
                self._test_fields_converter.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenbizmockDesensitiveQueryResponse, self).parse_response_content(response_content)
        if 'test_field_converter' in response:
            self.test_field_converter = response['test_field_converter']
        if 'test_fields_converter' in response:
            self.test_fields_converter = response['test_fields_converter']
