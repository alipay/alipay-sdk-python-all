#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPaiProxyRedirectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPaiProxyRedirectResponse, self).__init__()
        self._test_res = None

    @property
    def test_res(self):
        return self._test_res

    @test_res.setter
    def test_res(self, value):
        self._test_res = value

    def parse_response_content(self, response_content):
        response = super(AlipayPaiProxyRedirectResponse, self).parse_response_content(response_content)
        if 'test_res' in response:
            self.test_res = response['test_res']
