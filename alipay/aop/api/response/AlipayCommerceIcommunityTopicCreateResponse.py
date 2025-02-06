#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIcommunityTopicCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIcommunityTopicCreateResponse, self).__init__()
        self._out_request_id = None
        self._topic_id = None

    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def topic_id(self):
        return self._topic_id

    @topic_id.setter
    def topic_id(self, value):
        self._topic_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIcommunityTopicCreateResponse, self).parse_response_content(response_content)
        if 'out_request_id' in response:
            self.out_request_id = response['out_request_id']
        if 'topic_id' in response:
            self.topic_id = response['topic_id']
