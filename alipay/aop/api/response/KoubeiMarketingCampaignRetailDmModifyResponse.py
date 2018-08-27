#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignRetailDmModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignRetailDmModifyResponse, self).__init__()
        self._content_id = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignRetailDmModifyResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
