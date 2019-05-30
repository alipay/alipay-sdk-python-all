#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAntdataassetsCloudjobstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAntdataassetsCloudjobstatusQueryResponse, self).__init__()
        self._error_message = None
        self._status = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAntdataassetsCloudjobstatusQueryResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'status' in response:
            self.status = response['status']
