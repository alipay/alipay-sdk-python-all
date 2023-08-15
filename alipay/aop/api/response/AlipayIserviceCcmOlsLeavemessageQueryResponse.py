#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmOlsLeavemessageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmOlsLeavemessageQueryResponse, self).__init__()
        self._exist_unread_message = None
        self._unread_message_number = None

    @property
    def exist_unread_message(self):
        return self._exist_unread_message

    @exist_unread_message.setter
    def exist_unread_message(self, value):
        self._exist_unread_message = value
    @property
    def unread_message_number(self):
        return self._unread_message_number

    @unread_message_number.setter
    def unread_message_number(self, value):
        self._unread_message_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmOlsLeavemessageQueryResponse, self).parse_response_content(response_content)
        if 'exist_unread_message' in response:
            self.exist_unread_message = response['exist_unread_message']
        if 'unread_message_number' in response:
            self.unread_message_number = response['unread_message_number']
