#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignCashCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignCashCreateResponse, self).__init__()
        self._crowd_no = None
        self._origin_crowd_no = None
        self._pay_url = None

    @property
    def crowd_no(self):
        return self._crowd_no

    @crowd_no.setter
    def crowd_no(self, value):
        self._crowd_no = value
    @property
    def origin_crowd_no(self):
        return self._origin_crowd_no

    @origin_crowd_no.setter
    def origin_crowd_no(self, value):
        self._origin_crowd_no = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignCashCreateResponse, self).parse_response_content(response_content)
        if 'crowd_no' in response:
            self.crowd_no = response['crowd_no']
        if 'origin_crowd_no' in response:
            self.origin_crowd_no = response['origin_crowd_no']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
