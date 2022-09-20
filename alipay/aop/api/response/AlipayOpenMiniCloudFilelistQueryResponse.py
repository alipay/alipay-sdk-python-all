#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FileBaseInfoResponse import FileBaseInfoResponse


class AlipayOpenMiniCloudFilelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudFilelistQueryResponse, self).__init__()
        self._file_base_info_response_list = None
        self._next_token = None
        self._page_size = None

    @property
    def file_base_info_response_list(self):
        return self._file_base_info_response_list

    @file_base_info_response_list.setter
    def file_base_info_response_list(self, value):
        if isinstance(value, list):
            self._file_base_info_response_list = list()
            for i in value:
                if isinstance(i, FileBaseInfoResponse):
                    self._file_base_info_response_list.append(i)
                else:
                    self._file_base_info_response_list.append(FileBaseInfoResponse.from_alipay_dict(i))
    @property
    def next_token(self):
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudFilelistQueryResponse, self).parse_response_content(response_content)
        if 'file_base_info_response_list' in response:
            self.file_base_info_response_list = response['file_base_info_response_list']
        if 'next_token' in response:
            self.next_token = response['next_token']
        if 'page_size' in response:
            self.page_size = response['page_size']
