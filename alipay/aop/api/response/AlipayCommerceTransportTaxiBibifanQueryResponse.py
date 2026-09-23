#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaxiOrderDetail import TaxiOrderDetail
from alipay.aop.api.domain.TaxiRewardDetail import TaxiRewardDetail


class AlipayCommerceTransportTaxiBibifanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiBibifanQueryResponse, self).__init__()
        self._driver_id = None
        self._is_enrolled = None
        self._taxi_order_details = None
        self._taxi_reward_details = None

    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        self._driver_id = value
    @property
    def is_enrolled(self):
        return self._is_enrolled

    @is_enrolled.setter
    def is_enrolled(self, value):
        self._is_enrolled = value
    @property
    def taxi_order_details(self):
        return self._taxi_order_details

    @taxi_order_details.setter
    def taxi_order_details(self, value):
        if isinstance(value, list):
            self._taxi_order_details = list()
            for i in value:
                if isinstance(i, TaxiOrderDetail):
                    self._taxi_order_details.append(i)
                else:
                    self._taxi_order_details.append(TaxiOrderDetail.from_alipay_dict(i))
    @property
    def taxi_reward_details(self):
        return self._taxi_reward_details

    @taxi_reward_details.setter
    def taxi_reward_details(self, value):
        if isinstance(value, list):
            self._taxi_reward_details = list()
            for i in value:
                if isinstance(i, TaxiRewardDetail):
                    self._taxi_reward_details.append(i)
                else:
                    self._taxi_reward_details.append(TaxiRewardDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiBibifanQueryResponse, self).parse_response_content(response_content)
        if 'driver_id' in response:
            self.driver_id = response['driver_id']
        if 'is_enrolled' in response:
            self.is_enrolled = response['is_enrolled']
        if 'taxi_order_details' in response:
            self.taxi_order_details = response['taxi_order_details']
        if 'taxi_reward_details' in response:
            self.taxi_reward_details = response['taxi_reward_details']
