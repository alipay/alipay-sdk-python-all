#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotSdarttoolMessageSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotSdarttoolMessageSendResponse, self).__init__()
        self._message_no = None

    @property
    def message_no(self):
        return self._message_no

    @message_no.setter
    def message_no(self, value):
        self._message_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotSdarttoolMessageSendResponse, self).parse_response_content(response_content)
        if 'message_no' in response:
            self.message_no = response['message_no']
