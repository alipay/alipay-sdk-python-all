#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthAppAesSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthAppAesSetResponse, self).__init__()
        self._aes_key = None

    @property
    def aes_key(self):
        return self._aes_key

    @aes_key.setter
    def aes_key(self, value):
        self._aes_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthAppAesSetResponse, self).parse_response_content(response_content)
        if 'aes_key' in response:
            self.aes_key = response['aes_key']
