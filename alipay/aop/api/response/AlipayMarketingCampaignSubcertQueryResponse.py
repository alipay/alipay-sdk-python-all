#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubCertDetail import SubCertDetail


class AlipayMarketingCampaignSubcertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignSubcertQueryResponse, self).__init__()
        self._subcert_list = None
        self._total_num = None

    @property
    def subcert_list(self):
        return self._subcert_list

    @subcert_list.setter
    def subcert_list(self, value):
        if isinstance(value, list):
            self._subcert_list = list()
            for i in value:
                if isinstance(i, SubCertDetail):
                    self._subcert_list.append(i)
                else:
                    self._subcert_list.append(SubCertDetail.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignSubcertQueryResponse, self).parse_response_content(response_content)
        if 'subcert_list' in response:
            self.subcert_list = response['subcert_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
