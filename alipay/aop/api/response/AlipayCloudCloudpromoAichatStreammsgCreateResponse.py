#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChatData import ChatData


class AlipayCloudCloudpromoAichatStreammsgCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAichatStreammsgCreateResponse, self).__init__()
        self._data = None
        self._event = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, ChatData):
            self._data = value
        else:
            self._data = ChatData.from_alipay_dict(value)
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAichatStreammsgCreateResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'event' in response:
            self.event = response['event']
