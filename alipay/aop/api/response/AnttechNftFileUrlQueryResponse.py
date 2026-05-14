#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftFileUrlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftFileUrlQueryResponse, self).__init__()
        self._file_token = None
        self._url = None

    @property
    def file_token(self):
        return self._file_token

    @file_token.setter
    def file_token(self, value):
        self._file_token = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftFileUrlQueryResponse, self).parse_response_content(response_content)
        if 'file_token' in response:
            self.file_token = response['file_token']
        if 'url' in response:
            self.url = response['url']
