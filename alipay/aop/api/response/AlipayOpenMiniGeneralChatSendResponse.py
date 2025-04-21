#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeChatContent import AmpeChatContent


class AlipayOpenMiniGeneralChatSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniGeneralChatSendResponse, self).__init__()
        self._data = None
        self._event = None
        self._id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, AmpeChatContent):
            self._data = value
        else:
            self._data = AmpeChatContent.from_alipay_dict(value)
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniGeneralChatSendResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'event' in response:
            self.event = response['event']
        if 'id' in response:
            self.id = response['id']
