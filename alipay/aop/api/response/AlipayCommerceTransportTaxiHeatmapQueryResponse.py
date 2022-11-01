#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HeatMapData import HeatMapData


class AlipayCommerceTransportTaxiHeatmapQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiHeatmapQueryResponse, self).__init__()
        self._heatmap_data = None

    @property
    def heatmap_data(self):
        return self._heatmap_data

    @heatmap_data.setter
    def heatmap_data(self, value):
        if isinstance(value, HeatMapData):
            self._heatmap_data = value
        else:
            self._heatmap_data = HeatMapData.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiHeatmapQueryResponse, self).parse_response_content(response_content)
        if 'heatmap_data' in response:
            self.heatmap_data = response['heatmap_data']
