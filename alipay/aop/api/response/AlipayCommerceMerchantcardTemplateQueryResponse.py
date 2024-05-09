#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantCardTemplate import MerchantCardTemplate


class AlipayCommerceMerchantcardTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardTemplateQueryResponse, self).__init__()
        self._card_template = None

    @property
    def card_template(self):
        return self._card_template

    @card_template.setter
    def card_template(self, value):
        if isinstance(value, MerchantCardTemplate):
            self._card_template = value
        else:
            self._card_template = MerchantCardTemplate.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardTemplateQueryResponse, self).parse_response_content(response_content)
        if 'card_template' in response:
            self.card_template = response['card_template']
