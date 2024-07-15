#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneChannelsaleVoucherCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneChannelsaleVoucherCreateResponse, self).__init__()
        self._effect_end_time = None
        self._effect_start_time = None
        self._voucher_code = None
        self._voucher_url = None

    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value
    @property
    def voucher_url(self):
        return self._voucher_url

    @voucher_url.setter
    def voucher_url(self, value):
        self._voucher_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneChannelsaleVoucherCreateResponse, self).parse_response_content(response_content)
        if 'effect_end_time' in response:
            self.effect_end_time = response['effect_end_time']
        if 'effect_start_time' in response:
            self.effect_start_time = response['effect_start_time']
        if 'voucher_code' in response:
            self.voucher_code = response['voucher_code']
        if 'voucher_url' in response:
            self.voucher_url = response['voucher_url']
