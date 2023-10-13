#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAittestOpenapiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAittestOpenapiQueryResponse, self).__init__()
        self._demo_content = None
        self._demo_msg = None
        self._id = None

    @property
    def demo_content(self):
        return self._demo_content

    @demo_content.setter
    def demo_content(self, value):
        self._demo_content = value
    @property
    def demo_msg(self):
        return self._demo_msg

    @demo_msg.setter
    def demo_msg(self, value):
        self._demo_msg = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAittestOpenapiQueryResponse, self).parse_response_content(response_content)
        if 'demo_content' in response:
            self.demo_content = response['demo_content']
        if 'demo_msg' in response:
            self.demo_msg = response['demo_msg']
        if 'id' in response:
            self.id = response['id']
