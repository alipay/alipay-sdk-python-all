#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalFileAccessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalFileAccessQueryResponse, self).__init__()
        self._file_url_list = None

    @property
    def file_url_list(self):
        return self._file_url_list

    @file_url_list.setter
    def file_url_list(self, value):
        if isinstance(value, list):
            self._file_url_list = list()
            for i in value:
                self._file_url_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalFileAccessQueryResponse, self).parse_response_content(response_content)
        if 'file_url_list' in response:
            self.file_url_list = response['file_url_list']
