#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityCommunityinfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityCommunityinfoCreateResponse, self).__init__()
        self._community_short_name = None
        self._community_url = None

    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def community_url(self):
        return self._community_url

    @community_url.setter
    def community_url(self, value):
        self._community_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityCommunityinfoCreateResponse, self).parse_response_content(response_content)
        if 'community_short_name' in response:
            self.community_short_name = response['community_short_name']
        if 'community_url' in response:
            self.community_url = response['community_url']
