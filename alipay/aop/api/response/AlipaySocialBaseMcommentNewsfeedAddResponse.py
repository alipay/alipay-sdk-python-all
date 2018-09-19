#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseMcommentNewsfeedAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseMcommentNewsfeedAddResponse, self).__init__()
        self._newsfeed_id = None

    @property
    def newsfeed_id(self):
        return self._newsfeed_id

    @newsfeed_id.setter
    def newsfeed_id(self, value):
        self._newsfeed_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseMcommentNewsfeedAddResponse, self).parse_response_content(response_content)
        if 'newsfeed_id' in response:
            self.newsfeed_id = response['newsfeed_id']
