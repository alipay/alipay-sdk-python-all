#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationCarservicesaastldcAuthenticationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationCarservicesaastldcAuthenticationQueryResponse, self).__init__()
        self._auth_no = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationCarservicesaastldcAuthenticationQueryResponse, self).parse_response_content(response_content)
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
