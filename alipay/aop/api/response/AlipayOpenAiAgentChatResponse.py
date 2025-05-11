#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReplyPayload import ReplyPayload


class AlipayOpenAiAgentChatResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAiAgentChatResponse, self).__init__()
        self._event_type = None
        self._payloads = None
        self._turn = None

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def payloads(self):
        return self._payloads

    @payloads.setter
    def payloads(self, value):
        if isinstance(value, ReplyPayload):
            self._payloads = value
        else:
            self._payloads = ReplyPayload.from_alipay_dict(value)
    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAiAgentChatResponse, self).parse_response_content(response_content)
        if 'event_type' in response:
            self.event_type = response['event_type']
        if 'payloads' in response:
            self.payloads = response['payloads']
        if 'turn' in response:
            self.turn = response['turn']
