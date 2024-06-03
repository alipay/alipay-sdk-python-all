#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCardCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCardCancelResponse, self).__init__()
        self._process_id = None
        self._status = None

    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCardCancelResponse, self).parse_response_content(response_content)
        if 'process_id' in response:
            self.process_id = response['process_id']
        if 'status' in response:
            self.status = response['status']
