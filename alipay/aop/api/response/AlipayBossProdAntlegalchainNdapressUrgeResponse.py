#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlegalchainNdapressUrgeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainNdapressUrgeResponse, self).__init__()
        self._press_status = None

    @property
    def press_status(self):
        return self._press_status

    @press_status.setter
    def press_status(self, value):
        self._press_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainNdapressUrgeResponse, self).parse_response_content(response_content)
        if 'press_status' in response:
            self.press_status = response['press_status']
