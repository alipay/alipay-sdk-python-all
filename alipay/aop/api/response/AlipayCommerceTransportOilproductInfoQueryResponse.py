#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OilStationDetails import OilStationDetails


class AlipayCommerceTransportOilproductInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOilproductInfoQueryResponse, self).__init__()
        self._oil_station_models = None

    @property
    def oil_station_models(self):
        return self._oil_station_models

    @oil_station_models.setter
    def oil_station_models(self, value):
        if isinstance(value, OilStationDetails):
            self._oil_station_models = value
        else:
            self._oil_station_models = OilStationDetails.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOilproductInfoQueryResponse, self).parse_response_content(response_content)
        if 'oil_station_models' in response:
            self.oil_station_models = response['oil_station_models']
