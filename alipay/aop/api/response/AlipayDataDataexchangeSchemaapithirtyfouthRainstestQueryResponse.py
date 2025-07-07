#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataexchangeSchemaapithirtyfouthRainstestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeSchemaapithirtyfouthRainstestQueryResponse, self).__init__()
        self._demo = None
        self._open_id = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeSchemaapithirtyfouthRainstestQueryResponse, self).parse_response_content(response_content)
        if 'demo' in response:
            self.demo = response['demo']
        if 'open_id' in response:
            self.open_id = response['open_id']
