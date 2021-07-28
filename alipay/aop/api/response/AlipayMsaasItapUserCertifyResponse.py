#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItapResponsePayload import ItapResponsePayload


class AlipayMsaasItapUserCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasItapUserCertifyResponse, self).__init__()
        self._payload = None
        self._request_id = None

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        if isinstance(value, list):
            self._payload = list()
            for i in value:
                if isinstance(i, ItapResponsePayload):
                    self._payload.append(i)
                else:
                    self._payload.append(ItapResponsePayload.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasItapUserCertifyResponse, self).parse_response_content(response_content)
        if 'payload' in response:
            self.payload = response['payload']
        if 'request_id' in response:
            self.request_id = response['request_id']
