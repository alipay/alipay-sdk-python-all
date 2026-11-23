#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPublicAttachSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPublicAttachSyncResponse, self).__init__()
        self._file_path_list = None

    @property
    def file_path_list(self):
        return self._file_path_list

    @file_path_list.setter
    def file_path_list(self, value):
        if isinstance(value, list):
            self._file_path_list = list()
            for i in value:
                self._file_path_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPublicAttachSyncResponse, self).parse_response_content(response_content)
        if 'file_path_list' in response:
            self.file_path_list = response['file_path_list']
