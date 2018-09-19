#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignCertCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignCertCreateResponse, self).__init__()
        self._lot_number = None

    @property
    def lot_number(self):
        return self._lot_number

    @lot_number.setter
    def lot_number(self, value):
        self._lot_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignCertCreateResponse, self).parse_response_content(response_content)
        if 'lot_number' in response:
            self.lot_number = response['lot_number']
