#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardTemplateInfo import CardTemplateInfo


class AlipayCommerceCardTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCardTemplateQueryResponse, self).__init__()
        self._card_template_info = None

    @property
    def card_template_info(self):
        return self._card_template_info

    @card_template_info.setter
    def card_template_info(self, value):
        if isinstance(value, CardTemplateInfo):
            self._card_template_info = value
        else:
            self._card_template_info = CardTemplateInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCardTemplateQueryResponse, self).parse_response_content(response_content)
        if 'card_template_info' in response:
            self.card_template_info = response['card_template_info']
