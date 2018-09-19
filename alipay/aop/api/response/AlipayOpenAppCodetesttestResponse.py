#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppCodetesttestResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppCodetesttestResponse, self).__init__()
        self._testtesttest = None

    @property
    def testtesttest(self):
        return self._testtesttest

    @testtesttest.setter
    def testtesttest(self, value):
        self._testtesttest = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppCodetesttestResponse, self).parse_response_content(response_content)
        if 'testtesttest' in response:
            self.testtesttest = response['testtesttest']
