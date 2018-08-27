#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayZdatafrontDatatransferedFileuploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayZdatafrontDatatransferedFileuploadResponse, self).__init__()
        self._result_data = None
        self._success = None

    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        self._result_data = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayZdatafrontDatatransferedFileuploadResponse, self).parse_response_content(response_content)
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'success' in response:
            self.success = response['success']
