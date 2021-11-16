#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseFileUrlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseFileUrlGetResponse, self).__init__()
        self._file_name = None
        self._target_file_id = None
        self._url = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def target_file_id(self):
        return self._target_file_id

    @target_file_id.setter
    def target_file_id(self, value):
        self._target_file_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseFileUrlGetResponse, self).parse_response_content(response_content)
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'target_file_id' in response:
            self.target_file_id = response['target_file_id']
        if 'url' in response:
            self.url = response['url']
