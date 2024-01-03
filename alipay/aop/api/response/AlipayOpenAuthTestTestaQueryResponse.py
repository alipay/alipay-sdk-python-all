#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthTestTestaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthTestTestaQueryResponse, self).__init__()
        self._test = None

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthTestTestaQueryResponse, self).parse_response_content(response_content)
        if 'test' in response:
            self.test = response['test']
