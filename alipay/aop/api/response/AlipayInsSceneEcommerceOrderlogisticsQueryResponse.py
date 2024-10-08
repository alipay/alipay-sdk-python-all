#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenLogisticsDigestDTO import InsOpenLogisticsDigestDTO


class AlipayInsSceneEcommerceOrderlogisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceOrderlogisticsQueryResponse, self).__init__()
        self._logistics_digest = None

    @property
    def logistics_digest(self):
        return self._logistics_digest

    @logistics_digest.setter
    def logistics_digest(self, value):
        if isinstance(value, InsOpenLogisticsDigestDTO):
            self._logistics_digest = value
        else:
            self._logistics_digest = InsOpenLogisticsDigestDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceOrderlogisticsQueryResponse, self).parse_response_content(response_content)
        if 'logistics_digest' in response:
            self.logistics_digest = response['logistics_digest']
