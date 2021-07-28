#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataIotdataSearchlibraryBaiUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataSearchlibraryBaiUploadResponse, self).__init__()
        self._update_desc = None
        self._update_result = None

    @property
    def update_desc(self):
        return self._update_desc

    @update_desc.setter
    def update_desc(self, value):
        self._update_desc = value
    @property
    def update_result(self):
        return self._update_result

    @update_result.setter
    def update_result(self, value):
        self._update_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataSearchlibraryBaiUploadResponse, self).parse_response_content(response_content)
        if 'update_desc' in response:
            self.update_desc = response['update_desc']
        if 'update_result' in response:
            self.update_result = response['update_result']
