#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIservicePromotioncoreChatCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIservicePromotioncoreChatCreateResponse, self).__init__()
        self._message_content = None
        self._message_id = None

    @property
    def message_content(self):
        return self._message_content

    @message_content.setter
    def message_content(self, value):
        self._message_content = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIservicePromotioncoreChatCreateResponse, self).parse_response_content(response_content)
        if 'message_content' in response:
            self.message_content = response['message_content']
        if 'message_id' in response:
            self.message_id = response['message_id']
