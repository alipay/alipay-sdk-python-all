#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryRecruitSettlementSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRecruitSettlementSyncResponse, self).__init__()
        self._settlement_id = None

    @property
    def settlement_id(self):
        return self._settlement_id

    @settlement_id.setter
    def settlement_id(self, value):
        self._settlement_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRecruitSettlementSyncResponse, self).parse_response_content(response_content)
        if 'settlement_id' in response:
            self.settlement_id = response['settlement_id']
