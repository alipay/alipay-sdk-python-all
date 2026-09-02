#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayVoyagerIndustryOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerIndustryOrderSyncResponse, self).__init__()
        self._consume_status = None
        self._error_code = None
        self._need_retry = None

    @property
    def consume_status(self):
        return self._consume_status

    @consume_status.setter
    def consume_status(self, value):
        self._consume_status = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def need_retry(self):
        return self._need_retry

    @need_retry.setter
    def need_retry(self, value):
        self._need_retry = value

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerIndustryOrderSyncResponse, self).parse_response_content(response_content)
        if 'consume_status' in response:
            self.consume_status = response['consume_status']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'need_retry' in response:
            self.need_retry = response['need_retry']
