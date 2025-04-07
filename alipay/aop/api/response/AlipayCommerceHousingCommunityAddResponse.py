#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHousingCommunityAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHousingCommunityAddResponse, self).__init__()
        self._community_id = None

    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHousingCommunityAddResponse, self).parse_response_content(response_content)
        if 'community_id' in response:
            self.community_id = response['community_id']
