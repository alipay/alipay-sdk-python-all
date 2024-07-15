#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoAichatFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAichatFileUploadResponse, self).__init__()
        self._file_id = None
        self._file_tag = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_tag(self):
        return self._file_tag

    @file_tag.setter
    def file_tag(self, value):
        self._file_tag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAichatFileUploadResponse, self).parse_response_content(response_content)
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'file_tag' in response:
            self.file_tag = response['file_tag']
