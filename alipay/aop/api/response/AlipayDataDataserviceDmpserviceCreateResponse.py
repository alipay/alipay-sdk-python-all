#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceDmpserviceCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDmpserviceCreateResponse, self).__init__()
        self._event_time = None
        self._status = None

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDmpserviceCreateResponse, self).parse_response_content(response_content)
        if 'event_time' in response:
            self.event_time = response['event_time']
        if 'status' in response:
            self.status = response['status']
