#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEntertainmentCardSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEntertainmentCardSyncResponse, self).__init__()
        self._card_id = None
        self._idempotent = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEntertainmentCardSyncResponse, self).parse_response_content(response_content)
        if 'card_id' in response:
            self.card_id = response['card_id']
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
