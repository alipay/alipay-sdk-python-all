#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertdocUrlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertdocUrlQueryResponse, self).__init__()
        self._url = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertdocUrlQueryResponse, self).parse_response_content(response_content)
        if 'url' in response:
            self.url = response['url']
