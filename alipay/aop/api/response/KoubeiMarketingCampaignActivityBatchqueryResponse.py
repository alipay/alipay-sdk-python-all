#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CampBaseDto import CampBaseDto


class KoubeiMarketingCampaignActivityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignActivityBatchqueryResponse, self).__init__()
        self._camp_sets = None
        self._total_number = None

    @property
    def camp_sets(self):
        return self._camp_sets

    @camp_sets.setter
    def camp_sets(self, value):
        if isinstance(value, list):
            self._camp_sets = list()
            for i in value:
                if isinstance(i, CampBaseDto):
                    self._camp_sets.append(i)
                else:
                    self._camp_sets.append(CampBaseDto.from_alipay_dict(i))
    @property
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignActivityBatchqueryResponse, self).parse_response_content(response_content)
        if 'camp_sets' in response:
            self.camp_sets = response['camp_sets']
        if 'total_number' in response:
            self.total_number = response['total_number']
