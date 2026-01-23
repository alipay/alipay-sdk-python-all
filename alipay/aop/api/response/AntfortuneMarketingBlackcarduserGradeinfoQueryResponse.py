#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneMarketingBlackcarduserGradeinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneMarketingBlackcarduserGradeinfoQueryResponse, self).__init__()
        self._auth_result = None

    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        self._auth_result = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneMarketingBlackcarduserGradeinfoQueryResponse, self).parse_response_content(response_content)
        if 'auth_result' in response:
            self.auth_result = response['auth_result']
