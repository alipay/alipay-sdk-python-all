#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCardConsumeSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardConsumeSyncResponse, self).__init__()
        self._external_card_no = None

    @property
    def external_card_no(self):
        return self._external_card_no

    @external_card_no.setter
    def external_card_no(self, value):
        self._external_card_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardConsumeSyncResponse, self).parse_response_content(response_content)
        if 'external_card_no' in response:
            self.external_card_no = response['external_card_no']
