#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserAddressInfoObj import UserAddressInfoObj
from alipay.aop.api.domain.SelectedStationInfoDTO import SelectedStationInfoDTO
from alipay.aop.api.domain.UserAddressInfoObj import UserAddressInfoObj
from alipay.aop.api.domain.ServiceInfoObj import ServiceInfoObj


class AlipayCommerceLogisticsTokenInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsTokenInfoQueryResponse, self).__init__()
        self._receive_info = None
        self._selected_station_info = None
        self._send_info = None
        self._service_info = None

    @property
    def receive_info(self):
        return self._receive_info

    @receive_info.setter
    def receive_info(self, value):
        if isinstance(value, UserAddressInfoObj):
            self._receive_info = value
        else:
            self._receive_info = UserAddressInfoObj.from_alipay_dict(value)
    @property
    def selected_station_info(self):
        return self._selected_station_info

    @selected_station_info.setter
    def selected_station_info(self, value):
        if isinstance(value, SelectedStationInfoDTO):
            self._selected_station_info = value
        else:
            self._selected_station_info = SelectedStationInfoDTO.from_alipay_dict(value)
    @property
    def send_info(self):
        return self._send_info

    @send_info.setter
    def send_info(self, value):
        if isinstance(value, UserAddressInfoObj):
            self._send_info = value
        else:
            self._send_info = UserAddressInfoObj.from_alipay_dict(value)
    @property
    def service_info(self):
        return self._service_info

    @service_info.setter
    def service_info(self, value):
        if isinstance(value, ServiceInfoObj):
            self._service_info = value
        else:
            self._service_info = ServiceInfoObj.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsTokenInfoQueryResponse, self).parse_response_content(response_content)
        if 'receive_info' in response:
            self.receive_info = response['receive_info']
        if 'selected_station_info' in response:
            self.selected_station_info = response['selected_station_info']
        if 'send_info' in response:
            self.send_info = response['send_info']
        if 'service_info' in response:
            self.service_info = response['service_info']
