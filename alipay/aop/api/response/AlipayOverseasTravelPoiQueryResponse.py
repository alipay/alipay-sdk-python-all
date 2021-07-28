#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoiQueryResult import PoiQueryResult


class AlipayOverseasTravelPoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelPoiQueryResponse, self).__init__()
        self._poi_query_result = None

    @property
    def poi_query_result(self):
        return self._poi_query_result

    @poi_query_result.setter
    def poi_query_result(self, value):
        if isinstance(value, PoiQueryResult):
            self._poi_query_result = value
        else:
            self._poi_query_result = PoiQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelPoiQueryResponse, self).parse_response_content(response_content)
        if 'poi_query_result' in response:
            self.poi_query_result = response['poi_query_result']
