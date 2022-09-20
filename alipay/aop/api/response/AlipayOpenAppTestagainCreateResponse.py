#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestagainCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestagainCreateResponse, self).__init__()
        self._buyer_id = None
        self._buyer_openid = None
        self._test = None
        self._test_openid = None
        self._xxxxxx = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_openid(self):
        return self._buyer_openid

    @buyer_openid.setter
    def buyer_openid(self, value):
        self._buyer_openid = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def test_openid(self):
        return self._test_openid

    @test_openid.setter
    def test_openid(self, value):
        self._test_openid = value
    @property
    def xxxxxx(self):
        return self._xxxxxx

    @xxxxxx.setter
    def xxxxxx(self, value):
        self._xxxxxx = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestagainCreateResponse, self).parse_response_content(response_content)
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'buyer_openid' in response:
            self.buyer_openid = response['buyer_openid']
        if 'test' in response:
            self.test = response['test']
        if 'test_openid' in response:
            self.test_openid = response['test_openid']
        if 'xxxxxx' in response:
            self.xxxxxx = response['xxxxxx']
