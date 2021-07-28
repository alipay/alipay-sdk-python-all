#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDataCampaignSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataCampaignSendResponse, self).__init__()
        self._sub_status = None

    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataCampaignSendResponse, self).parse_response_content(response_content)
        if 'sub_status' in response:
            self.sub_status = response['sub_status']
