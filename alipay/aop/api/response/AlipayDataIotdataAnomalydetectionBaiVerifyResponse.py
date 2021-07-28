#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataIotdataAnomalydetectionBaiVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataIotdataAnomalydetectionBaiVerifyResponse, self).__init__()
        self._event_detail = None
        self._event_type = None

    @property
    def event_detail(self):
        return self._event_detail

    @event_detail.setter
    def event_detail(self, value):
        self._event_detail = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataIotdataAnomalydetectionBaiVerifyResponse, self).parse_response_content(response_content)
        if 'event_detail' in response:
            self.event_detail = response['event_detail']
        if 'event_type' in response:
            self.event_type = response['event_type']
