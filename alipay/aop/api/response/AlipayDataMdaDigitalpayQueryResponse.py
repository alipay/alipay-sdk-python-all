#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaDigitalpayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaDigitalpayQueryResponse, self).__init__()
        self._asian_village_trd_cnt = None
        self._mmc_trd_cnt = None
        self._total_trd_cnt = None
        self._trd_cnt_trend = None
        self._venue_trd_cnt = None

    @property
    def asian_village_trd_cnt(self):
        return self._asian_village_trd_cnt

    @asian_village_trd_cnt.setter
    def asian_village_trd_cnt(self, value):
        self._asian_village_trd_cnt = value
    @property
    def mmc_trd_cnt(self):
        return self._mmc_trd_cnt

    @mmc_trd_cnt.setter
    def mmc_trd_cnt(self, value):
        self._mmc_trd_cnt = value
    @property
    def total_trd_cnt(self):
        return self._total_trd_cnt

    @total_trd_cnt.setter
    def total_trd_cnt(self, value):
        self._total_trd_cnt = value
    @property
    def trd_cnt_trend(self):
        return self._trd_cnt_trend

    @trd_cnt_trend.setter
    def trd_cnt_trend(self, value):
        self._trd_cnt_trend = value
    @property
    def venue_trd_cnt(self):
        return self._venue_trd_cnt

    @venue_trd_cnt.setter
    def venue_trd_cnt(self, value):
        self._venue_trd_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaDigitalpayQueryResponse, self).parse_response_content(response_content)
        if 'asian_village_trd_cnt' in response:
            self.asian_village_trd_cnt = response['asian_village_trd_cnt']
        if 'mmc_trd_cnt' in response:
            self.mmc_trd_cnt = response['mmc_trd_cnt']
        if 'total_trd_cnt' in response:
            self.total_trd_cnt = response['total_trd_cnt']
        if 'trd_cnt_trend' in response:
            self.trd_cnt_trend = response['trd_cnt_trend']
        if 'venue_trd_cnt' in response:
            self.venue_trd_cnt = response['venue_trd_cnt']
