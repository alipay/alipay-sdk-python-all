#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateFacefeatureFileApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateFacefeatureFileApplyResponse, self).__init__()
        self._download_url = None
        self._file_date = None
        self._file_name = None
        self._file_status = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def file_date(self):
        return self._file_date

    @file_date.setter
    def file_date(self, value):
        self._file_date = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_status(self):
        return self._file_status

    @file_status.setter
    def file_status(self, value):
        self._file_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateFacefeatureFileApplyResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'file_date' in response:
            self.file_date = response['file_date']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'file_status' in response:
            self.file_status = response['file_status']
