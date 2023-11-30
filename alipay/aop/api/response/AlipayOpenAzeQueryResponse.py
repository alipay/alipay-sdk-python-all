#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAzeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAzeQueryResponse, self).__init__()
        self._key_word = None
        self._result = None

    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, value):
        self._key_word = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAzeQueryResponse, self).parse_response_content(response_content)
        if 'key_word' in response:
            self.key_word = response['key_word']
        if 'result' in response:
            self.result = response['result']
