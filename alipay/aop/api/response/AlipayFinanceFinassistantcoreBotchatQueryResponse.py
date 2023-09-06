#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZXBBotChatResult import ZXBBotChatResult


class AlipayFinanceFinassistantcoreBotchatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFinassistantcoreBotchatQueryResponse, self).__init__()
        self._zxb_chat_response = None

    @property
    def zxb_chat_response(self):
        return self._zxb_chat_response

    @zxb_chat_response.setter
    def zxb_chat_response(self, value):
        if isinstance(value, ZXBBotChatResult):
            self._zxb_chat_response = value
        else:
            self._zxb_chat_response = ZXBBotChatResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFinassistantcoreBotchatQueryResponse, self).parse_response_content(response_content)
        if 'zxb_chat_response' in response:
            self.zxb_chat_response = response['zxb_chat_response']
