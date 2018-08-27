#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsMarketingCampaignPrizeSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingCampaignPrizeSendResponse, self).__init__()
        self._asset_id = None
        self._compaign_id = None
        self._coupon_id = None
        self._coupon_type = None
        self._coupon_value = None
        self._flow_id = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def compaign_id(self):
        return self._compaign_id

    @compaign_id.setter
    def compaign_id(self, value):
        self._compaign_id = value
    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self._coupon_id = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def coupon_value(self):
        return self._coupon_value

    @coupon_value.setter
    def coupon_value(self, value):
        self._coupon_value = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingCampaignPrizeSendResponse, self).parse_response_content(response_content)
        if 'asset_id' in response:
            self.asset_id = response['asset_id']
        if 'compaign_id' in response:
            self.compaign_id = response['compaign_id']
        if 'coupon_id' in response:
            self.coupon_id = response['coupon_id']
        if 'coupon_type' in response:
            self.coupon_type = response['coupon_type']
        if 'coupon_value' in response:
            self.coupon_value = response['coupon_value']
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
