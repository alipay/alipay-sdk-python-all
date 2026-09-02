#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbikeChargeStation import EbikeChargeStation


class AlipayCommerceTransportEbikeChargestationdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEbikeChargestationdetailQueryResponse, self).__init__()
        self._ebike_charge_station_detail = None

    @property
    def ebike_charge_station_detail(self):
        return self._ebike_charge_station_detail

    @ebike_charge_station_detail.setter
    def ebike_charge_station_detail(self, value):
        if isinstance(value, EbikeChargeStation):
            self._ebike_charge_station_detail = value
        else:
            self._ebike_charge_station_detail = EbikeChargeStation.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEbikeChargestationdetailQueryResponse, self).parse_response_content(response_content)
        if 'ebike_charge_station_detail' in response:
            self.ebike_charge_station_detail = response['ebike_charge_station_detail']
