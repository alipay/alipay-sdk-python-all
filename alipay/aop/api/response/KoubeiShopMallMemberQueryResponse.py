#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiShopMallMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopMallMemberQueryResponse, self).__init__()
        self._card_level = None
        self._card_name = None
        self._card_point = None
        self._has_card = None
        self._trade_authed = None

    @property
    def card_level(self):
        return self._card_level

    @card_level.setter
    def card_level(self, value):
        self._card_level = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_point(self):
        return self._card_point

    @card_point.setter
    def card_point(self, value):
        self._card_point = value
    @property
    def has_card(self):
        return self._has_card

    @has_card.setter
    def has_card(self, value):
        self._has_card = value
    @property
    def trade_authed(self):
        return self._trade_authed

    @trade_authed.setter
    def trade_authed(self, value):
        self._trade_authed = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopMallMemberQueryResponse, self).parse_response_content(response_content)
        if 'card_level' in response:
            self.card_level = response['card_level']
        if 'card_name' in response:
            self.card_name = response['card_name']
        if 'card_point' in response:
            self.card_point = response['card_point']
        if 'has_card' in response:
            self.has_card = response['has_card']
        if 'trade_authed' in response:
            self.trade_authed = response['trade_authed']
