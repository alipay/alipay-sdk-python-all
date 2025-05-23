#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdcampaignCreativeCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignCreativeCreateormodifyResponse, self).__init__()
        self._creative_id = None
        self._creative_name = None

    @property
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, value):
        self._creative_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignCreativeCreateormodifyResponse, self).parse_response_content(response_content)
        if 'creative_id' in response:
            self.creative_id = response['creative_id']
        if 'creative_name' in response:
            self.creative_name = response['creative_name']
