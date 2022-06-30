#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectIotQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectIotQueryResponse, self).__init__()
        self._content_id = None
        self._content_type = None
        self._text = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectIotQueryResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'content_type' in response:
            self.content_type = response['content_type']
        if 'text' in response:
            self.text = response['text']
