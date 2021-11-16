#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportTaxiDriverauthenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiDriverauthenQueryResponse, self).__init__()
        self._bind_status = None
        self._driver_id = None
        self._driver_user_id = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        self._driver_id = value
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiDriverauthenQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'driver_id' in response:
            self.driver_id = response['driver_id']
        if 'driver_user_id' in response:
            self.driver_user_id = response['driver_user_id']
