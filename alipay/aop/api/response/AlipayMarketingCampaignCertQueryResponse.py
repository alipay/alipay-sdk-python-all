#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KnCertSendOrderDetail import KnCertSendOrderDetail


class AlipayMarketingCampaignCertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignCertQueryResponse, self).__init__()
        self._subcert_list = None
        self._total_remain_point = None

    @property
    def subcert_list(self):
        return self._subcert_list

    @subcert_list.setter
    def subcert_list(self, value):
        if isinstance(value, list):
            self._subcert_list = list()
            for i in value:
                if isinstance(i, KnCertSendOrderDetail):
                    self._subcert_list.append(i)
                else:
                    self._subcert_list.append(KnCertSendOrderDetail.from_alipay_dict(i))
    @property
    def total_remain_point(self):
        return self._total_remain_point

    @total_remain_point.setter
    def total_remain_point(self, value):
        self._total_remain_point = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignCertQueryResponse, self).parse_response_content(response_content)
        if 'subcert_list' in response:
            self.subcert_list = response['subcert_list']
        if 'total_remain_point' in response:
            self.total_remain_point = response['total_remain_point']
