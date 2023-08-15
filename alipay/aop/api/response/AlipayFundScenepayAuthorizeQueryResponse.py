#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundScenepayAuthorizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundScenepayAuthorizeQueryResponse, self).__init__()
        self._authorization_id = None
        self._status = None

    @property
    def authorization_id(self):
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, value):
        self._authorization_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundScenepayAuthorizeQueryResponse, self).parse_response_content(response_content)
        if 'authorization_id' in response:
            self.authorization_id = response['authorization_id']
        if 'status' in response:
            self.status = response['status']
