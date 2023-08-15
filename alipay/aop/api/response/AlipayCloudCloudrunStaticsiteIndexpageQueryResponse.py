#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunStaticsiteIndexpageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteIndexpageQueryResponse, self).__init__()
        self._index_file = None

    @property
    def index_file(self):
        return self._index_file

    @index_file.setter
    def index_file(self, value):
        self._index_file = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteIndexpageQueryResponse, self).parse_response_content(response_content)
        if 'index_file' in response:
            self.index_file = response['index_file']
