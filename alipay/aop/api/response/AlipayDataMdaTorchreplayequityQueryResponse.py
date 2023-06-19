#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplayequityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplayequityQueryResponse, self).__init__()
        self._equity_prize_distribute = None
        self._equity_pv = None
        self._equity_uv = None
        self._search_uv = None
        self._search_uv_trend = None
        self._torchbearer_clothing_cnt = None

    @property
    def equity_prize_distribute(self):
        return self._equity_prize_distribute

    @equity_prize_distribute.setter
    def equity_prize_distribute(self, value):
        self._equity_prize_distribute = value
    @property
    def equity_pv(self):
        return self._equity_pv

    @equity_pv.setter
    def equity_pv(self, value):
        self._equity_pv = value
    @property
    def equity_uv(self):
        return self._equity_uv

    @equity_uv.setter
    def equity_uv(self, value):
        self._equity_uv = value
    @property
    def search_uv(self):
        return self._search_uv

    @search_uv.setter
    def search_uv(self, value):
        self._search_uv = value
    @property
    def search_uv_trend(self):
        return self._search_uv_trend

    @search_uv_trend.setter
    def search_uv_trend(self, value):
        self._search_uv_trend = value
    @property
    def torchbearer_clothing_cnt(self):
        return self._torchbearer_clothing_cnt

    @torchbearer_clothing_cnt.setter
    def torchbearer_clothing_cnt(self, value):
        self._torchbearer_clothing_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplayequityQueryResponse, self).parse_response_content(response_content)
        if 'equity_prize_distribute' in response:
            self.equity_prize_distribute = response['equity_prize_distribute']
        if 'equity_pv' in response:
            self.equity_pv = response['equity_pv']
        if 'equity_uv' in response:
            self.equity_uv = response['equity_uv']
        if 'search_uv' in response:
            self.search_uv = response['search_uv']
        if 'search_uv_trend' in response:
            self.search_uv_trend = response['search_uv_trend']
        if 'torchbearer_clothing_cnt' in response:
            self.torchbearer_clothing_cnt = response['torchbearer_clothing_cnt']
