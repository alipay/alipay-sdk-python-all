#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignRetailDmCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignRetailDmCreateResponse, self).__init__()
        self._content_id = None
        self._ext_info = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignRetailDmCreateResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
