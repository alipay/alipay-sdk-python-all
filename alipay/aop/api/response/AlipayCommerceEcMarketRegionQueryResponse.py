#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenMarketingRegionDTO import OpenMarketingRegionDTO


class AlipayCommerceEcMarketRegionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcMarketRegionQueryResponse, self).__init__()
        self._region_info = None

    @property
    def region_info(self):
        return self._region_info

    @region_info.setter
    def region_info(self, value):
        if isinstance(value, OpenMarketingRegionDTO):
            self._region_info = value
        else:
            self._region_info = OpenMarketingRegionDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcMarketRegionQueryResponse, self).parse_response_content(response_content)
        if 'region_info' in response:
            self.region_info = response['region_info']
