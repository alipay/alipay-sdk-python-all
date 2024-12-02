#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppOpenbizmocktoolsDanielQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenbizmocktoolsDanielQueryResponse, self).__init__()
        self._hello = None

    @property
    def hello(self):
        return self._hello

    @hello.setter
    def hello(self, value):
        self._hello = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenbizmocktoolsDanielQueryResponse, self).parse_response_content(response_content)
        if 'hello' in response:
            self.hello = response['hello']
