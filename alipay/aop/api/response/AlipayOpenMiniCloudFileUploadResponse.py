#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniCloudFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudFileUploadResponse, self).__init__()
        self._download_url = None
        self._file_id = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudFileUploadResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'file_id' in response:
            self.file_id = response['file_id']
