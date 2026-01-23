#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialMemberCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialMemberCheckResponse, self).__init__()
        self._card_id = None
        self._card_no = None
        self._card_status = None
        self._expire_time = None
        self._open = None
        self._open_time = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialMemberCheckResponse, self).parse_response_content(response_content)
        if 'card_id' in response:
            self.card_id = response['card_id']
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'card_status' in response:
            self.card_status = response['card_status']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'open' in response:
            self.open = response['open']
        if 'open_time' in response:
            self.open_time = response['open_time']
