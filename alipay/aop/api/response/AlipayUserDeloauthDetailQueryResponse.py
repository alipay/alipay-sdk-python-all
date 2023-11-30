#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DelOauthDetailResult import DelOauthDetailResult


class AlipayUserDeloauthDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDeloauthDetailQueryResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, DelOauthDetailResult):
            self._response = value
        else:
            self._response = DelOauthDetailResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserDeloauthDetailQueryResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
