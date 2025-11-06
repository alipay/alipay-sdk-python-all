#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTourIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourIdentityQueryResponse, self).__init__()
        self._identity_result = None

    @property
    def identity_result(self):
        return self._identity_result

    @identity_result.setter
    def identity_result(self, value):
        self._identity_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourIdentityQueryResponse, self).parse_response_content(response_content)
        if 'identity_result' in response:
            self.identity_result = response['identity_result']
