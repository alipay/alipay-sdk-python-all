#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiShopMallMemberIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopMallMemberIdentifyResponse, self).__init__()
        self._card_no = None
        self._has_card = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def has_card(self):
        return self._has_card

    @has_card.setter
    def has_card(self, value):
        self._has_card = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopMallMemberIdentifyResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'has_card' in response:
            self.has_card = response['has_card']
