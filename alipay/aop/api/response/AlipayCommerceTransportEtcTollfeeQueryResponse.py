#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcTollFeeTollStatsDTO import EtcTollFeeTollStatsDTO


class AlipayCommerceTransportEtcTollfeeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcTollfeeQueryResponse, self).__init__()
        self._end_city = None
        self._end_station = None
        self._start_city = None
        self._start_station = None
        self._toll_stats = None

    @property
    def end_city(self):
        return self._end_city

    @end_city.setter
    def end_city(self, value):
        self._end_city = value
    @property
    def end_station(self):
        return self._end_station

    @end_station.setter
    def end_station(self, value):
        self._end_station = value
    @property
    def start_city(self):
        return self._start_city

    @start_city.setter
    def start_city(self, value):
        self._start_city = value
    @property
    def start_station(self):
        return self._start_station

    @start_station.setter
    def start_station(self, value):
        self._start_station = value
    @property
    def toll_stats(self):
        return self._toll_stats

    @toll_stats.setter
    def toll_stats(self, value):
        if isinstance(value, EtcTollFeeTollStatsDTO):
            self._toll_stats = value
        else:
            self._toll_stats = EtcTollFeeTollStatsDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcTollfeeQueryResponse, self).parse_response_content(response_content)
        if 'end_city' in response:
            self.end_city = response['end_city']
        if 'end_station' in response:
            self.end_station = response['end_station']
        if 'start_city' in response:
            self.start_city = response['start_city']
        if 'start_station' in response:
            self.start_station = response['start_station']
        if 'toll_stats' in response:
            self.toll_stats = response['toll_stats']
