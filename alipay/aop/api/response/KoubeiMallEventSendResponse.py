#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMallEventSendResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallEventSendResponse, self).__init__()
        self._event_id = None

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMallEventSendResponse, self).parse_response_content(response_content)
        if 'event_id' in response:
            self.event_id = response['event_id']
