#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthAuthenticationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthAuthenticationQueryResponse, self).__init__()
        self._identity_result = None
        self._identity_result_skip_url = None

    @property
    def identity_result(self):
        return self._identity_result

    @identity_result.setter
    def identity_result(self, value):
        self._identity_result = value
    @property
    def identity_result_skip_url(self):
        return self._identity_result_skip_url

    @identity_result_skip_url.setter
    def identity_result_skip_url(self, value):
        self._identity_result_skip_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthAuthenticationQueryResponse, self).parse_response_content(response_content)
        if 'identity_result' in response:
            self.identity_result = response['identity_result']
        if 'identity_result_skip_url' in response:
            self.identity_result_skip_url = response['identity_result_skip_url']
