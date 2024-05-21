#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechAmpAigcApplyResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechAmpAigcApplyResponse, self).__init__()
        self._file_url = None
        self._other_data = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def other_data(self):
        return self._other_data

    @other_data.setter
    def other_data(self, value):
        self._other_data = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechAmpAigcApplyResponse, self).parse_response_content(response_content)
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'other_data' in response:
            self.other_data = response['other_data']
