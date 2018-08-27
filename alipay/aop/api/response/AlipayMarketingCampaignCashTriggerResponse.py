#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignCashTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignCashTriggerResponse, self).__init__()
        self._biz_no = None
        self._coupon_name = None
        self._error_msg = None
        self._merchant_logo = None
        self._out_biz_no = None
        self._partner_id = None
        self._prize_amount = None
        self._prize_msg = None
        self._repeat_trigger_flag = None
        self._trigger_result = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def coupon_name(self):
        return self._coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self._coupon_name = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def prize_amount(self):
        return self._prize_amount

    @prize_amount.setter
    def prize_amount(self, value):
        self._prize_amount = value
    @property
    def prize_msg(self):
        return self._prize_msg

    @prize_msg.setter
    def prize_msg(self, value):
        self._prize_msg = value
    @property
    def repeat_trigger_flag(self):
        return self._repeat_trigger_flag

    @repeat_trigger_flag.setter
    def repeat_trigger_flag(self, value):
        self._repeat_trigger_flag = value
    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignCashTriggerResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'coupon_name' in response:
            self.coupon_name = response['coupon_name']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'merchant_logo' in response:
            self.merchant_logo = response['merchant_logo']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'prize_amount' in response:
            self.prize_amount = response['prize_amount']
        if 'prize_msg' in response:
            self.prize_msg = response['prize_msg']
        if 'repeat_trigger_flag' in response:
            self.repeat_trigger_flag = response['repeat_trigger_flag']
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
