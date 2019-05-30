#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneServiceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneServiceOrderQueryResponse, self).__init__()
        self._alipay_trade_no = None
        self._effect_end_time = None
        self._effect_start_time = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneServiceOrderQueryResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'effect_end_time' in response:
            self.effect_end_time = response['effect_end_time']
        if 'effect_start_time' in response:
            self.effect_start_time = response['effect_start_time']
