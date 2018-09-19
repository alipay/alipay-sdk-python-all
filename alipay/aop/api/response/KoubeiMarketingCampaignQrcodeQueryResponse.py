#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignQrcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignQrcodeQueryResponse, self).__init__()
        self._qrcode_url = None

    @property
    def qrcode_url(self):
        return self._qrcode_url

    @qrcode_url.setter
    def qrcode_url(self, value):
        self._qrcode_url = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignQrcodeQueryResponse, self).parse_response_content(response_content)
        if 'qrcode_url' in response:
            self.qrcode_url = response['qrcode_url']
