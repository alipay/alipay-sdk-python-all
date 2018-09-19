#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataexchangeDtmorseSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeDtmorseSyncResponse, self).__init__()
        self._result_extent = None
        self._success = None

    @property
    def result_extent(self):
        return self._result_extent

    @result_extent.setter
    def result_extent(self, value):
        self._result_extent = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeDtmorseSyncResponse, self).parse_response_content(response_content)
        if 'result_extent' in response:
            self.result_extent = response['result_extent']
        if 'success' in response:
            self.success = response['success']
