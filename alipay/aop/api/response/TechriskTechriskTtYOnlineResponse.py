#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ManjiangTestabc import ManjiangTestabc


class TechriskTechriskTtYOnlineResponse(AlipayResponse):

    def __init__(self):
        super(TechriskTechriskTtYOnlineResponse, self).__init__()
        self._s = None
        self._test = None
        self._test_open_id = None

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        if isinstance(value, ManjiangTestabc):
            self._s = value
        else:
            self._s = ManjiangTestabc.from_alipay_dict(value)
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def test_open_id(self):
        return self._test_open_id

    @test_open_id.setter
    def test_open_id(self, value):
        self._test_open_id = value

    def parse_response_content(self, response_content):
        response = super(TechriskTechriskTtYOnlineResponse, self).parse_response_content(response_content)
        if 's' in response:
            self.s = response['s']
        if 'test' in response:
            self.test = response['test']
        if 'test_open_id' in response:
            self.test_open_id = response['test_open_id']
