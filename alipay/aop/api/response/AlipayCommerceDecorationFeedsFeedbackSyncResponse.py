#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDecorationFeedsFeedbackSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDecorationFeedsFeedbackSyncResponse, self).__init__()
        self._feedback_type = None
        self._lead_id = None
        self._sync_message = None

    @property
    def feedback_type(self):
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, value):
        self._feedback_type = value
    @property
    def lead_id(self):
        return self._lead_id

    @lead_id.setter
    def lead_id(self, value):
        self._lead_id = value
    @property
    def sync_message(self):
        return self._sync_message

    @sync_message.setter
    def sync_message(self, value):
        self._sync_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDecorationFeedsFeedbackSyncResponse, self).parse_response_content(response_content)
        if 'feedback_type' in response:
            self.feedback_type = response['feedback_type']
        if 'lead_id' in response:
            self.lead_id = response['lead_id']
        if 'sync_message' in response:
            self.sync_message = response['sync_message']
