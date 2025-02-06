#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIcommunityContentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIcommunityContentCreateResponse, self).__init__()
        self._icommunity_content_id = None
        self._out_content_id = None

    @property
    def icommunity_content_id(self):
        return self._icommunity_content_id

    @icommunity_content_id.setter
    def icommunity_content_id(self, value):
        self._icommunity_content_id = value
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIcommunityContentCreateResponse, self).parse_response_content(response_content)
        if 'icommunity_content_id' in response:
            self.icommunity_content_id = response['icommunity_content_id']
        if 'out_content_id' in response:
            self.out_content_id = response['out_content_id']
