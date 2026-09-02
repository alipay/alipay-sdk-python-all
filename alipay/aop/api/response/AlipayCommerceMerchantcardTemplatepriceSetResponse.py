#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardTemplatepriceSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardTemplatepriceSetResponse, self).__init__()
        self._card_template_id = None
        self._success_count = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardTemplatepriceSetResponse, self).parse_response_content(response_content)
        if 'card_template_id' in response:
            self.card_template_id = response['card_template_id']
        if 'success_count' in response:
            self.success_count = response['success_count']
