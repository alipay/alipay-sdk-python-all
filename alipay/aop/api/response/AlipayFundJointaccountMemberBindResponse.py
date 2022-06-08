#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountMemberBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountMemberBindResponse, self).__init__()
        self._reply_url = None

    @property
    def reply_url(self):
        return self._reply_url

    @reply_url.setter
    def reply_url(self, value):
        self._reply_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountMemberBindResponse, self).parse_response_content(response_content)
        if 'reply_url' in response:
            self.reply_url = response['reply_url']
