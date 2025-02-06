#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityThirdpartycommunityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityThirdpartycommunityCreateResponse, self).__init__()
        self._community_id = None
        self._community_short_name = None
        self._property_company_short_name = None

    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def property_company_short_name(self):
        return self._property_company_short_name

    @property_company_short_name.setter
    def property_company_short_name(self, value):
        self._property_company_short_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityThirdpartycommunityCreateResponse, self).parse_response_content(response_content)
        if 'community_id' in response:
            self.community_id = response['community_id']
        if 'community_short_name' in response:
            self.community_short_name = response['community_short_name']
        if 'property_company_short_name' in response:
            self.property_company_short_name = response['property_company_short_name']
