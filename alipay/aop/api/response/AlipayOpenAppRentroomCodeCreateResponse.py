#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppRentroomCodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppRentroomCodeCreateResponse, self).__init__()
        self._share_token = None

    @property
    def share_token(self):
        return self._share_token

    @share_token.setter
    def share_token(self, value):
        self._share_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppRentroomCodeCreateResponse, self).parse_response_content(response_content)
        if 'share_token' in response:
            self.share_token = response['share_token']
