#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExRefRateInfoVO import ExRefRateInfoVO


class AlipayAccountExrateRatequeryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateRatequeryResponse, self).__init__()
        self._rate_query_response_list = None

    @property
    def rate_query_response_list(self):
        return self._rate_query_response_list

    @rate_query_response_list.setter
    def rate_query_response_list(self, value):
        if isinstance(value, list):
            self._rate_query_response_list = list()
            for i in value:
                if isinstance(i, ExRefRateInfoVO):
                    self._rate_query_response_list.append(i)
                else:
                    self._rate_query_response_list.append(ExRefRateInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateRatequeryResponse, self).parse_response_content(response_content)
        if 'rate_query_response_list' in response:
            self.rate_query_response_list = response['rate_query_response_list']
