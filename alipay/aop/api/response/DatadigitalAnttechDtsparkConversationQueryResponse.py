#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MessageDetail import MessageDetail


class DatadigitalAnttechDtsparkConversationQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechDtsparkConversationQueryResponse, self).__init__()
        self._messages = None

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, value):
        if isinstance(value, list):
            self._messages = list()
            for i in value:
                if isinstance(i, MessageDetail):
                    self._messages.append(i)
                else:
                    self._messages.append(MessageDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechDtsparkConversationQueryResponse, self).parse_response_content(response_content)
        if 'messages' in response:
            self.messages = response['messages']
