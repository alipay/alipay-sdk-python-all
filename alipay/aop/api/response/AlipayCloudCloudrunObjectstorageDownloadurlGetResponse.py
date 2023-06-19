#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DownloadUrlResponse import DownloadUrlResponse


class AlipayCloudCloudrunObjectstorageDownloadurlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageDownloadurlGetResponse, self).__init__()
        self._file_list = None

    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, DownloadUrlResponse):
                    self._file_list.append(i)
                else:
                    self._file_list.append(DownloadUrlResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageDownloadurlGetResponse, self).parse_response_content(response_content)
        if 'file_list' in response:
            self.file_list = response['file_list']
