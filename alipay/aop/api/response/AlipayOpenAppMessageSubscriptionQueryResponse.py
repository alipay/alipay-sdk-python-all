#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppMessageSubscriptionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppMessageSubscriptionQueryResponse, self).__init__()
        self._comm_type = None
        self._tag = None
        self._topic = None

    @property
    def comm_type(self):
        return self._comm_type

    @comm_type.setter
    def comm_type(self, value):
        self._comm_type = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        self._topic = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppMessageSubscriptionQueryResponse, self).parse_response_content(response_content)
        if 'comm_type' in response:
            self.comm_type = response['comm_type']
        if 'tag' in response:
            self.tag = response['tag']
        if 'topic' in response:
            self.topic = response['topic']
