#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCardActivateurlApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardActivateurlApplyResponse, self).__init__()
        self._apply_card_url = None

    @property
    def apply_card_url(self):
        return self._apply_card_url

    @apply_card_url.setter
    def apply_card_url(self, value):
        self._apply_card_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardActivateurlApplyResponse, self).parse_response_content(response_content)
        if 'apply_card_url' in response:
            self.apply_card_url = response['apply_card_url']
