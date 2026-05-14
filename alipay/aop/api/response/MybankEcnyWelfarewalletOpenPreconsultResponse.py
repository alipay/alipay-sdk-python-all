#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyWelfarewalletOpenPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyWelfarewalletOpenPreconsultResponse, self).__init__()
        self._allow_show = None
        self._has_wallet = None
        self._open_wallet_url = None
        self._refuse_reason = None

    @property
    def allow_show(self):
        return self._allow_show

    @allow_show.setter
    def allow_show(self, value):
        self._allow_show = value
    @property
    def has_wallet(self):
        return self._has_wallet

    @has_wallet.setter
    def has_wallet(self, value):
        self._has_wallet = value
    @property
    def open_wallet_url(self):
        return self._open_wallet_url

    @open_wallet_url.setter
    def open_wallet_url(self, value):
        self._open_wallet_url = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyWelfarewalletOpenPreconsultResponse, self).parse_response_content(response_content)
        if 'allow_show' in response:
            self.allow_show = response['allow_show']
        if 'has_wallet' in response:
            self.has_wallet = response['has_wallet']
        if 'open_wallet_url' in response:
            self.open_wallet_url = response['open_wallet_url']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
