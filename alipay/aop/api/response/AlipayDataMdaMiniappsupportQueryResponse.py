#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniappsupportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniappsupportQueryResponse, self).__init__()
        self._ai_service_ratio = None
        self._customer_satisfaction = None
        self._manual_service_ratio = None
        self._today_ai_service_cnt = None
        self._today_manual_service_cnt = None
        self._today_service_trend = None
        self._total_ai_service_cnt = None
        self._total_manual_service_cnt = None
        self._word_cloud = None
        self._yesterday_ai_service_cnt = None
        self._yesterday_manual_service_cnt = None
        self._yesterday_service_trend = None

    @property
    def ai_service_ratio(self):
        return self._ai_service_ratio

    @ai_service_ratio.setter
    def ai_service_ratio(self, value):
        self._ai_service_ratio = value
    @property
    def customer_satisfaction(self):
        return self._customer_satisfaction

    @customer_satisfaction.setter
    def customer_satisfaction(self, value):
        self._customer_satisfaction = value
    @property
    def manual_service_ratio(self):
        return self._manual_service_ratio

    @manual_service_ratio.setter
    def manual_service_ratio(self, value):
        self._manual_service_ratio = value
    @property
    def today_ai_service_cnt(self):
        return self._today_ai_service_cnt

    @today_ai_service_cnt.setter
    def today_ai_service_cnt(self, value):
        self._today_ai_service_cnt = value
    @property
    def today_manual_service_cnt(self):
        return self._today_manual_service_cnt

    @today_manual_service_cnt.setter
    def today_manual_service_cnt(self, value):
        self._today_manual_service_cnt = value
    @property
    def today_service_trend(self):
        return self._today_service_trend

    @today_service_trend.setter
    def today_service_trend(self, value):
        self._today_service_trend = value
    @property
    def total_ai_service_cnt(self):
        return self._total_ai_service_cnt

    @total_ai_service_cnt.setter
    def total_ai_service_cnt(self, value):
        self._total_ai_service_cnt = value
    @property
    def total_manual_service_cnt(self):
        return self._total_manual_service_cnt

    @total_manual_service_cnt.setter
    def total_manual_service_cnt(self, value):
        self._total_manual_service_cnt = value
    @property
    def word_cloud(self):
        return self._word_cloud

    @word_cloud.setter
    def word_cloud(self, value):
        self._word_cloud = value
    @property
    def yesterday_ai_service_cnt(self):
        return self._yesterday_ai_service_cnt

    @yesterday_ai_service_cnt.setter
    def yesterday_ai_service_cnt(self, value):
        self._yesterday_ai_service_cnt = value
    @property
    def yesterday_manual_service_cnt(self):
        return self._yesterday_manual_service_cnt

    @yesterday_manual_service_cnt.setter
    def yesterday_manual_service_cnt(self, value):
        self._yesterday_manual_service_cnt = value
    @property
    def yesterday_service_trend(self):
        return self._yesterday_service_trend

    @yesterday_service_trend.setter
    def yesterday_service_trend(self, value):
        self._yesterday_service_trend = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniappsupportQueryResponse, self).parse_response_content(response_content)
        if 'ai_service_ratio' in response:
            self.ai_service_ratio = response['ai_service_ratio']
        if 'customer_satisfaction' in response:
            self.customer_satisfaction = response['customer_satisfaction']
        if 'manual_service_ratio' in response:
            self.manual_service_ratio = response['manual_service_ratio']
        if 'today_ai_service_cnt' in response:
            self.today_ai_service_cnt = response['today_ai_service_cnt']
        if 'today_manual_service_cnt' in response:
            self.today_manual_service_cnt = response['today_manual_service_cnt']
        if 'today_service_trend' in response:
            self.today_service_trend = response['today_service_trend']
        if 'total_ai_service_cnt' in response:
            self.total_ai_service_cnt = response['total_ai_service_cnt']
        if 'total_manual_service_cnt' in response:
            self.total_manual_service_cnt = response['total_manual_service_cnt']
        if 'word_cloud' in response:
            self.word_cloud = response['word_cloud']
        if 'yesterday_ai_service_cnt' in response:
            self.yesterday_ai_service_cnt = response['yesterday_ai_service_cnt']
        if 'yesterday_manual_service_cnt' in response:
            self.yesterday_manual_service_cnt = response['yesterday_manual_service_cnt']
        if 'yesterday_service_trend' in response:
            self.yesterday_service_trend = response['yesterday_service_trend']
