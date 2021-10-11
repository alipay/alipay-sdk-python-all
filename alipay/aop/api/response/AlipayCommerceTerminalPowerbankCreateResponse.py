#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTerminalPowerbankCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTerminalPowerbankCreateResponse, self).__init__()
        self._terminal_id = None

    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTerminalPowerbankCreateResponse, self).parse_response_content(response_content)
        if 'terminal_id' in response:
            self.terminal_id = response['terminal_id']
