#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataSmartactivityForecastResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataSmartactivityForecastResponse, self).__init__()
        self._apply_cnt_max = None
        self._apply_cnt_min = None
        self._increased_exposure_max = None
        self._increased_exposure_min = None
        self._repay_rate_range_max = None
        self._repay_rate_range_min = None
        self._trade_amt_range_max = None
        self._trade_amt_range_min = None
        self._verify_count_range_max = None
        self._verify_count_range_min = None

    @property
    def apply_cnt_max(self):
        return self._apply_cnt_max

    @apply_cnt_max.setter
    def apply_cnt_max(self, value):
        self._apply_cnt_max = value
    @property
    def apply_cnt_min(self):
        return self._apply_cnt_min

    @apply_cnt_min.setter
    def apply_cnt_min(self, value):
        self._apply_cnt_min = value
    @property
    def increased_exposure_max(self):
        return self._increased_exposure_max

    @increased_exposure_max.setter
    def increased_exposure_max(self, value):
        self._increased_exposure_max = value
    @property
    def increased_exposure_min(self):
        return self._increased_exposure_min

    @increased_exposure_min.setter
    def increased_exposure_min(self, value):
        self._increased_exposure_min = value
    @property
    def repay_rate_range_max(self):
        return self._repay_rate_range_max

    @repay_rate_range_max.setter
    def repay_rate_range_max(self, value):
        self._repay_rate_range_max = value
    @property
    def repay_rate_range_min(self):
        return self._repay_rate_range_min

    @repay_rate_range_min.setter
    def repay_rate_range_min(self, value):
        self._repay_rate_range_min = value
    @property
    def trade_amt_range_max(self):
        return self._trade_amt_range_max

    @trade_amt_range_max.setter
    def trade_amt_range_max(self, value):
        self._trade_amt_range_max = value
    @property
    def trade_amt_range_min(self):
        return self._trade_amt_range_min

    @trade_amt_range_min.setter
    def trade_amt_range_min(self, value):
        self._trade_amt_range_min = value
    @property
    def verify_count_range_max(self):
        return self._verify_count_range_max

    @verify_count_range_max.setter
    def verify_count_range_max(self, value):
        self._verify_count_range_max = value
    @property
    def verify_count_range_min(self):
        return self._verify_count_range_min

    @verify_count_range_min.setter
    def verify_count_range_min(self, value):
        self._verify_count_range_min = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataSmartactivityForecastResponse, self).parse_response_content(response_content)
        if 'apply_cnt_max' in response:
            self.apply_cnt_max = response['apply_cnt_max']
        if 'apply_cnt_min' in response:
            self.apply_cnt_min = response['apply_cnt_min']
        if 'increased_exposure_max' in response:
            self.increased_exposure_max = response['increased_exposure_max']
        if 'increased_exposure_min' in response:
            self.increased_exposure_min = response['increased_exposure_min']
        if 'repay_rate_range_max' in response:
            self.repay_rate_range_max = response['repay_rate_range_max']
        if 'repay_rate_range_min' in response:
            self.repay_rate_range_min = response['repay_rate_range_min']
        if 'trade_amt_range_max' in response:
            self.trade_amt_range_max = response['trade_amt_range_max']
        if 'trade_amt_range_min' in response:
            self.trade_amt_range_min = response['trade_amt_range_min']
        if 'verify_count_range_max' in response:
            self.verify_count_range_max = response['verify_count_range_max']
        if 'verify_count_range_min' in response:
            self.verify_count_range_min = response['verify_count_range_min']
