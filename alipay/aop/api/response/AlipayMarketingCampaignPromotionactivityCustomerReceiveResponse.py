#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignPromotionactivityCustomerReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPromotionactivityCustomerReceiveResponse, self).__init__()
        self._template_id = None
        self._voucher_id = None

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPromotionactivityCustomerReceiveResponse, self).parse_response_content(response_content)
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
