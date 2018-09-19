#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CampDetail import CampDetail


class KoubeiMarketingCampaignActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignActivityQueryResponse, self).__init__()
        self._camp_detail = None

    @property
    def camp_detail(self):
        return self._camp_detail

    @camp_detail.setter
    def camp_detail(self, value):
        if isinstance(value, CampDetail):
            self._camp_detail = value
        else:
            self._camp_detail = CampDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignActivityQueryResponse, self).parse_response_content(response_content)
        if 'camp_detail' in response:
            self.camp_detail = response['camp_detail']
