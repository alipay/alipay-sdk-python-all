#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherTemplate import VoucherTemplate


class AlipayMarketingCampaignSelfActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignSelfActivityQueryResponse, self).__init__()
        self._activity_end_time = None
        self._activity_name = None
        self._activity_start_time = None
        self._activity_status = None
        self._merchant_logo = None
        self._merchant_name = None
        self._voucher_template_list = None

    @property
    def activity_end_time(self):
        return self._activity_end_time

    @activity_end_time.setter
    def activity_end_time(self, value):
        self._activity_end_time = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_start_time(self):
        return self._activity_start_time

    @activity_start_time.setter
    def activity_start_time(self, value):
        self._activity_start_time = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def voucher_template_list(self):
        return self._voucher_template_list

    @voucher_template_list.setter
    def voucher_template_list(self, value):
        if isinstance(value, list):
            self._voucher_template_list = list()
            for i in value:
                if isinstance(i, VoucherTemplate):
                    self._voucher_template_list.append(i)
                else:
                    self._voucher_template_list.append(VoucherTemplate.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignSelfActivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_end_time' in response:
            self.activity_end_time = response['activity_end_time']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_start_time' in response:
            self.activity_start_time = response['activity_start_time']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'merchant_logo' in response:
            self.merchant_logo = response['merchant_logo']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'voucher_template_list' in response:
            self.voucher_template_list = response['voucher_template_list']
