#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignWarmcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignWarmcardQueryResponse, self).__init__()
        self._has_receive = None
        self._voucher_type_remain_info = None

    @property
    def has_receive(self):
        return self._has_receive

    @has_receive.setter
    def has_receive(self, value):
        self._has_receive = value
    @property
    def voucher_type_remain_info(self):
        return self._voucher_type_remain_info

    @voucher_type_remain_info.setter
    def voucher_type_remain_info(self, value):
        self._voucher_type_remain_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignWarmcardQueryResponse, self).parse_response_content(response_content)
        if 'has_receive' in response:
            self.has_receive = response['has_receive']
        if 'voucher_type_remain_info' in response:
            self.voucher_type_remain_info = response['voucher_type_remain_info']
