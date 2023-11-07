#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCardTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCardTemplateCreateResponse, self).__init__()
        self._card_template_id = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCardTemplateCreateResponse, self).parse_response_content(response_content)
        if 'card_template_id' in response:
            self.card_template_id = response['card_template_id']
