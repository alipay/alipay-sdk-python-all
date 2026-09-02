#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfimMqSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfimMqSyncResponse, self).__init__()
        self._tag = None
        self._topic = None

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
        response = super(AlipayCommerceMedicalHdfimMqSyncResponse, self).parse_response_content(response_content)
        if 'tag' in response:
            self.tag = response['tag']
        if 'topic' in response:
            self.topic = response['topic']
