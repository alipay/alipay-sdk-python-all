#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechAmpAigcQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechAmpAigcQueryResponse, self).__init__()
        self._file_url = None
        self._status = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechAmpAigcQueryResponse, self).parse_response_content(response_content)
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'status' in response:
            self.status = response['status']
