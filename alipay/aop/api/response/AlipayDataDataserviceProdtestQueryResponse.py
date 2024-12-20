#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceProdtestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceProdtestQueryResponse, self).__init__()
        self._user = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceProdtestQueryResponse, self).parse_response_content(response_content)
        if 'user' in response:
            self.user = response['user']
