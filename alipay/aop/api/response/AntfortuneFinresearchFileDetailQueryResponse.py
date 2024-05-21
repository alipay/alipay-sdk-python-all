#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneFinresearchFileDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchFileDetailQueryResponse, self).__init__()
        self._file_id = None
        self._file_name = None
        self._upload_status = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def upload_status(self):
        return self._upload_status

    @upload_status.setter
    def upload_status(self, value):
        self._upload_status = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchFileDetailQueryResponse, self).parse_response_content(response_content)
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'upload_status' in response:
            self.upload_status = response['upload_status']
