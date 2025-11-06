#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAlipayAmaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAlipayAmaQueryResponse, self).__init__()
        self._content = None
        self._finished = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value

    def parse_response_content(self, response_content):
        response = super(AlipayAlipayAmaQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'finished' in response:
            self.finished = response['finished']
