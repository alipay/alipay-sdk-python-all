#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaLefttrafficQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaLefttrafficQueryResponse, self).__init__()
        self._today_certificate_traffic_cnt = None
        self._total_certificate_traffic_unt = None
        self._total_ticket_traffic_unt = None
        self._totay_ticket_traffic_cnt = None
        self._traffic_day_trend = None
        self._traffic_hour_distribute = None
        self._traffic_paas = None

    @property
    def today_certificate_traffic_cnt(self):
        return self._today_certificate_traffic_cnt

    @today_certificate_traffic_cnt.setter
    def today_certificate_traffic_cnt(self, value):
        self._today_certificate_traffic_cnt = value
    @property
    def total_certificate_traffic_unt(self):
        return self._total_certificate_traffic_unt

    @total_certificate_traffic_unt.setter
    def total_certificate_traffic_unt(self, value):
        self._total_certificate_traffic_unt = value
    @property
    def total_ticket_traffic_unt(self):
        return self._total_ticket_traffic_unt

    @total_ticket_traffic_unt.setter
    def total_ticket_traffic_unt(self, value):
        self._total_ticket_traffic_unt = value
    @property
    def totay_ticket_traffic_cnt(self):
        return self._totay_ticket_traffic_cnt

    @totay_ticket_traffic_cnt.setter
    def totay_ticket_traffic_cnt(self, value):
        self._totay_ticket_traffic_cnt = value
    @property
    def traffic_day_trend(self):
        return self._traffic_day_trend

    @traffic_day_trend.setter
    def traffic_day_trend(self, value):
        self._traffic_day_trend = value
    @property
    def traffic_hour_distribute(self):
        return self._traffic_hour_distribute

    @traffic_hour_distribute.setter
    def traffic_hour_distribute(self, value):
        self._traffic_hour_distribute = value
    @property
    def traffic_paas(self):
        return self._traffic_paas

    @traffic_paas.setter
    def traffic_paas(self, value):
        self._traffic_paas = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaLefttrafficQueryResponse, self).parse_response_content(response_content)
        if 'today_certificate_traffic_cnt' in response:
            self.today_certificate_traffic_cnt = response['today_certificate_traffic_cnt']
        if 'total_certificate_traffic_unt' in response:
            self.total_certificate_traffic_unt = response['total_certificate_traffic_unt']
        if 'total_ticket_traffic_unt' in response:
            self.total_ticket_traffic_unt = response['total_ticket_traffic_unt']
        if 'totay_ticket_traffic_cnt' in response:
            self.totay_ticket_traffic_cnt = response['totay_ticket_traffic_cnt']
        if 'traffic_day_trend' in response:
            self.traffic_day_trend = response['traffic_day_trend']
        if 'traffic_hour_distribute' in response:
            self.traffic_hour_distribute = response['traffic_hour_distribute']
        if 'traffic_paas' in response:
            self.traffic_paas = response['traffic_paas']
