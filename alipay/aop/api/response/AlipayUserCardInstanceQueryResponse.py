#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCardInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCardInstanceQueryResponse, self).__init__()
        self._active_date = None
        self._balance = None
        self._card_status = None
        self._expiry_date = None
        self._level = None
        self._point = None
        self._template_id = None

    @property
    def active_date(self):
        return self._active_date

    @active_date.setter
    def active_date(self, value):
        self._active_date = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCardInstanceQueryResponse, self).parse_response_content(response_content)
        if 'active_date' in response:
            self.active_date = response['active_date']
        if 'balance' in response:
            self.balance = response['balance']
        if 'card_status' in response:
            self.card_status = response['card_status']
        if 'expiry_date' in response:
            self.expiry_date = response['expiry_date']
        if 'level' in response:
            self.level = response['level']
        if 'point' in response:
            self.point = response['point']
        if 'template_id' in response:
            self.template_id = response['template_id']
