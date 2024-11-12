#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFileConvertCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFileConvertCreateResponse, self).__init__()
        self._convert_task_id = None
        self._target_file_path = None

    @property
    def convert_task_id(self):
        return self._convert_task_id

    @convert_task_id.setter
    def convert_task_id(self, value):
        self._convert_task_id = value
    @property
    def target_file_path(self):
        return self._target_file_path

    @target_file_path.setter
    def target_file_path(self, value):
        self._target_file_path = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFileConvertCreateResponse, self).parse_response_content(response_content)
        if 'convert_task_id' in response:
            self.convert_task_id = response['convert_task_id']
        if 'target_file_path' in response:
            self.target_file_path = response['target_file_path']
