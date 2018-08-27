#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicContentPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicContentPublishResponse, self).__init__()
        self._message_id = None

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicContentPublishResponse, self).parse_response_content(response_content)
        if 'message_id' in response:
            self.message_id = response['message_id']
