#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdcampaignGroupCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignGroupCreateormodifyResponse, self).__init__()
        self._group_id = None
        self._group_name = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignGroupCreateormodifyResponse, self).parse_response_content(response_content)
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'group_name' in response:
            self.group_name = response['group_name']
