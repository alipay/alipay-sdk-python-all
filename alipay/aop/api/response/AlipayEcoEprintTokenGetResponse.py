#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEprintTokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEprintTokenGetResponse, self).__init__()
        self._eprint_token = None

    @property
    def eprint_token(self):
        return self._eprint_token

    @eprint_token.setter
    def eprint_token(self, value):
        self._eprint_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEprintTokenGetResponse, self).parse_response_content(response_content)
        if 'eprint_token' in response:
            self.eprint_token = response['eprint_token']
