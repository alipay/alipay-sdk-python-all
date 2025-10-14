#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalExchangeRedirectVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalExchangeRedirectVerifyResponse, self).__init__()
        self._card_no = None
        self._expire_time = None
        self._open = None
        self._phone = None
        self._redirect_url = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalExchangeRedirectVerifyResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'open' in response:
            self.open = response['open']
        if 'phone' in response:
            self.phone = response['phone']
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']
