#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestGraySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestGraySendResponse, self).__init__()
        self._open_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestGraySendResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
