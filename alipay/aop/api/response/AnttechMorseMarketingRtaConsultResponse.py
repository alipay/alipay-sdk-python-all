#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CampaignPrize import CampaignPrize


class AnttechMorseMarketingRtaConsultResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingRtaConsultResponse, self).__init__()
        self._admit = None
        self._biz_no = None
        self._campaign_prize = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def campaign_prize(self):
        return self._campaign_prize

    @campaign_prize.setter
    def campaign_prize(self, value):
        if isinstance(value, list):
            self._campaign_prize = list()
            for i in value:
                if isinstance(i, CampaignPrize):
                    self._campaign_prize.append(i)
                else:
                    self._campaign_prize.append(CampaignPrize.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingRtaConsultResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'campaign_prize' in response:
            self.campaign_prize = response['campaign_prize']
