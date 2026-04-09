#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderDeviceTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderDeviceTradeQueryResponse, self).__init__()
        self._alipay_trade_count = None
        self._device_sn = None
        self._smid = None
        self._touch_trade_count_range = None

    @property
    def alipay_trade_count(self):
        return self._alipay_trade_count

    @alipay_trade_count.setter
    def alipay_trade_count(self, value):
        self._alipay_trade_count = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def touch_trade_count_range(self):
        return self._touch_trade_count_range

    @touch_trade_count_range.setter
    def touch_trade_count_range(self, value):
        self._touch_trade_count_range = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderDeviceTradeQueryResponse, self).parse_response_content(response_content)
        if 'alipay_trade_count' in response:
            self.alipay_trade_count = response['alipay_trade_count']
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'smid' in response:
            self.smid = response['smid']
        if 'touch_trade_count_range' in response:
            self.touch_trade_count_range = response['touch_trade_count_range']
