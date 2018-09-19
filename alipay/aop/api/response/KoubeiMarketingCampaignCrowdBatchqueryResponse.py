#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignCrowdBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignCrowdBatchqueryResponse, self).__init__()
        self._crowd_group_sets = None
        self._total_number = None

    @property
    def crowd_group_sets(self):
        return self._crowd_group_sets

    @crowd_group_sets.setter
    def crowd_group_sets(self, value):
        self._crowd_group_sets = value
    @property
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignCrowdBatchqueryResponse, self).parse_response_content(response_content)
        if 'crowd_group_sets' in response:
            self.crowd_group_sets = response['crowd_group_sets']
        if 'total_number' in response:
            self.total_number = response['total_number']
