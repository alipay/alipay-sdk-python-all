#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicMessageContentModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicMessageContentModifyResponse, self).__init__()
        self._content_id = None
        self._content_url = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_url(self):
        return self._content_url

    @content_url.setter
    def content_url(self, value):
        self._content_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicMessageContentModifyResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'content_url' in response:
            self.content_url = response['content_url']
