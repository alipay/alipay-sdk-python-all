#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserTwostageIndirectUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserTwostageIndirectUseResponse, self).__init__()
        self._user_id = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserTwostageIndirectUseResponse, self).parse_response_content(response_content)
        if 'user_id' in response:
            self.user_id = response['user_id']
