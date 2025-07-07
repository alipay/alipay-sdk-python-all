#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocOperationOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocOperationOnlineResponse, self).__init__()
        self._verify_event_id = None

    @property
    def verify_event_id(self):
        return self._verify_event_id

    @verify_event_id.setter
    def verify_event_id(self, value):
        self._verify_event_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocOperationOnlineResponse, self).parse_response_content(response_content)
        if 'verify_event_id' in response:
            self.verify_event_id = response['verify_event_id']
