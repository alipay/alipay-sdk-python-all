#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InfoSecAnalyzeSyncResult import InfoSecAnalyzeSyncResult


class AlipaySecurityRiskContentAnalyzeSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskContentAnalyzeSyncResponse, self).__init__()
        self._req_msg_id = None
        self._response = None

    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, InfoSecAnalyzeSyncResult):
            self._response = value
        else:
            self._response = InfoSecAnalyzeSyncResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskContentAnalyzeSyncResponse, self).parse_response_content(response_content)
        if 'req_msg_id' in response:
            self.req_msg_id = response['req_msg_id']
        if 'response' in response:
            self.response = response['response']
