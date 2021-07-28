#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoFilePathQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoFilePathQueryResponse, self).__init__()
        self._file_id = None
        self._upload_url = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def upload_url(self):
        return self._upload_url

    @upload_url.setter
    def upload_url(self, value):
        self._upload_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoFilePathQueryResponse, self).parse_response_content(response_content)
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'upload_url' in response:
            self.upload_url = response['upload_url']
