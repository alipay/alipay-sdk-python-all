#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataShuanqQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataShuanqQueryResponse, self).__init__()
        self._cert_no = None
        self._name = None
        self._test = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataShuanqQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'name' in response:
            self.name = response['name']
        if 'test' in response:
            self.test = response['test']
