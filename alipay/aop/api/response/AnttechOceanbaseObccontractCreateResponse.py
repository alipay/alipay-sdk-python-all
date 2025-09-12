#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObccontractCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObccontractCreateResponse, self).__init__()
        self._file_url = None
        self._seal_request_id = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def seal_request_id(self):
        return self._seal_request_id

    @seal_request_id.setter
    def seal_request_id(self, value):
        self._seal_request_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObccontractCreateResponse, self).parse_response_content(response_content)
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'seal_request_id' in response:
            self.seal_request_id = response['seal_request_id']
