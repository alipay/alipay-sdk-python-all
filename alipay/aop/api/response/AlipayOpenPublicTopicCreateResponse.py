#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicTopicCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicTopicCreateResponse, self).__init__()
        self._topic_id = None

    @property
    def topic_id(self):
        return self._topic_id

    @topic_id.setter
    def topic_id(self, value):
        self._topic_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicTopicCreateResponse, self).parse_response_content(response_content)
        if 'topic_id' in response:
            self.topic_id = response['topic_id']
