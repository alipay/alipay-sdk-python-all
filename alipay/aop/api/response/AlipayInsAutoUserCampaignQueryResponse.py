#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoUserCampaignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoUserCampaignQueryResponse, self).__init__()
        self._register_status = None

    @property
    def register_status(self):
        return self._register_status

    @register_status.setter
    def register_status(self, value):
        self._register_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoUserCampaignQueryResponse, self).parse_response_content(response_content)
        if 'register_status' in response:
            self.register_status = response['register_status']
