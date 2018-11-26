#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdCreativeResult import AdCreativeResult


class AlipayCommerceTransportAdCreativeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdCreativeQueryResponse, self).__init__()
        self._ad_creative_result = None

    @property
    def ad_creative_result(self):
        return self._ad_creative_result

    @ad_creative_result.setter
    def ad_creative_result(self, value):
        if isinstance(value, AdCreativeResult):
            self._ad_creative_result = value
        else:
            self._ad_creative_result = AdCreativeResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdCreativeQueryResponse, self).parse_response_content(response_content)
        if 'ad_creative_result' in response:
            self.ad_creative_result = response['ad_creative_result']
