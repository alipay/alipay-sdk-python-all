#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunStaticsiteIndexpageModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteIndexpageModifyResponse, self).__init__()
        self._domain_list = None
        self._index_file = None

    @property
    def domain_list(self):
        return self._domain_list

    @domain_list.setter
    def domain_list(self, value):
        if isinstance(value, list):
            self._domain_list = list()
            for i in value:
                self._domain_list.append(i)
    @property
    def index_file(self):
        return self._index_file

    @index_file.setter
    def index_file(self, value):
        self._index_file = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteIndexpageModifyResponse, self).parse_response_content(response_content)
        if 'domain_list' in response:
            self.domain_list = response['domain_list']
        if 'index_file' in response:
            self.index_file = response['index_file']
