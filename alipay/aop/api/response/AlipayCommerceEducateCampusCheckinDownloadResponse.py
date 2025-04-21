#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusCheckinDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusCheckinDownloadResponse, self).__init__()
        self._file_path = None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusCheckinDownloadResponse, self).parse_response_content(response_content)
        if 'file_path' in response:
            self.file_path = response['file_path']
