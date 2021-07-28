#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiSelleradmitAdmittanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiSelleradmitAdmittanceQueryResponse, self).__init__()
        self._admit = None
        self._refuse_reason = None
        self._request_id = None
        self._request_key = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def request_key(self):
        return self._request_key

    @request_key.setter
    def request_key(self, value):
        self._request_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiSelleradmitAdmittanceQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'request_key' in response:
            self.request_key = response['request_key']
