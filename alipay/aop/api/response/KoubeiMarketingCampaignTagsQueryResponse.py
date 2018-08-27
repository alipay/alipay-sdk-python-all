#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignTagsQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignTagsQueryResponse, self).__init__()
        self._tags = None

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignTagsQueryResponse, self).parse_response_content(response_content)
        if 'tags' in response:
            self.tags = response['tags']
