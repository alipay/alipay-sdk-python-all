#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingPayinstCouponSendResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingPayinstCouponSendResponse, self).__init__()
        self._campaign_id = None
        self._coupon_id = None
        self._out_biz_id = None
        self._send_status = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingPayinstCouponSendResponse, self).parse_response_content(response_content)
        if 'campaign_id' in response:
            self.campaign_id = response['campaign_id']
        if 'coupon_id' in response:
            self.coupon_id = response['coupon_id']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'send_status' in response:
            self.send_status = response['send_status']
