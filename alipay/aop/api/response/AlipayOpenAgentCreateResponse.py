#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentCreateResponse, self).__init__()
        self._batch_no = None
        self._batch_status = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentCreateResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
