#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeAcpShortenurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeAcpShortenurlQueryResponse, self).__init__()
        self._shorten_url = None

    @property
    def shorten_url(self):
        return self._shorten_url

    @shorten_url.setter
    def shorten_url(self, value):
        self._shorten_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeAcpShortenurlQueryResponse, self).parse_response_content(response_content)
        if 'shorten_url' in response:
            self.shorten_url = response['shorten_url']
