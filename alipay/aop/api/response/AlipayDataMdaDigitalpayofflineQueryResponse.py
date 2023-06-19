#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaDigitalpayofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaDigitalpayofflineQueryResponse, self).__init__()
        self._cb_top_5_uv = None
        self._cb_total_uv = None
        self._cb_wallet_cnt = None
        self._top_5_merchant = None
        self._total_amount = None
        self._total_merchants = None
        self._total_trend = None

    @property
    def cb_top_5_uv(self):
        return self._cb_top_5_uv

    @cb_top_5_uv.setter
    def cb_top_5_uv(self, value):
        self._cb_top_5_uv = value
    @property
    def cb_total_uv(self):
        return self._cb_total_uv

    @cb_total_uv.setter
    def cb_total_uv(self, value):
        self._cb_total_uv = value
    @property
    def cb_wallet_cnt(self):
        return self._cb_wallet_cnt

    @cb_wallet_cnt.setter
    def cb_wallet_cnt(self, value):
        self._cb_wallet_cnt = value
    @property
    def top_5_merchant(self):
        return self._top_5_merchant

    @top_5_merchant.setter
    def top_5_merchant(self, value):
        self._top_5_merchant = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_merchants(self):
        return self._total_merchants

    @total_merchants.setter
    def total_merchants(self, value):
        self._total_merchants = value
    @property
    def total_trend(self):
        return self._total_trend

    @total_trend.setter
    def total_trend(self, value):
        self._total_trend = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaDigitalpayofflineQueryResponse, self).parse_response_content(response_content)
        if 'cb_top_5_uv' in response:
            self.cb_top_5_uv = response['cb_top_5_uv']
        if 'cb_total_uv' in response:
            self.cb_total_uv = response['cb_total_uv']
        if 'cb_wallet_cnt' in response:
            self.cb_wallet_cnt = response['cb_wallet_cnt']
        if 'top_5_merchant' in response:
            self.top_5_merchant = response['top_5_merchant']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_merchants' in response:
            self.total_merchants = response['total_merchants']
        if 'total_trend' in response:
            self.total_trend = response['total_trend']
