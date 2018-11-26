#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenEchoOfflineSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenEchoOfflineSendResponse, self).__init__()
        self._word = None

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, value):
        self._word = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenEchoOfflineSendResponse, self).parse_response_content(response_content)
        if 'word' in response:
            self.word = response['word']
