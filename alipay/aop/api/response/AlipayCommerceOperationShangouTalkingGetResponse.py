#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationShangouTalkingGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationShangouTalkingGetResponse, self).__init__()
        self._action_url = None
        self._result_text = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def result_text(self):
        return self._result_text

    @result_text.setter
    def result_text(self, value):
        self._result_text = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationShangouTalkingGetResponse, self).parse_response_content(response_content)
        if 'action_url' in response:
            self.action_url = response['action_url']
        if 'result_text' in response:
            self.result_text = response['result_text']
