#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCdpAdvertiseReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCdpAdvertiseReportQueryResponse, self).__init__()
        self._click_pv_dd = None
        self._click_pv_history = None
        self._click_uv_dd = None
        self._click_uv_history = None
        self._report_date = None
        self._show_pv_dd = None
        self._show_pv_history = None
        self._show_uv_dd = None
        self._show_uv_history = None

    @property
    def click_pv_dd(self):
        return self._click_pv_dd

    @click_pv_dd.setter
    def click_pv_dd(self, value):
        self._click_pv_dd = value
    @property
    def click_pv_history(self):
        return self._click_pv_history

    @click_pv_history.setter
    def click_pv_history(self, value):
        self._click_pv_history = value
    @property
    def click_uv_dd(self):
        return self._click_uv_dd

    @click_uv_dd.setter
    def click_uv_dd(self, value):
        self._click_uv_dd = value
    @property
    def click_uv_history(self):
        return self._click_uv_history

    @click_uv_history.setter
    def click_uv_history(self, value):
        self._click_uv_history = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def show_pv_dd(self):
        return self._show_pv_dd

    @show_pv_dd.setter
    def show_pv_dd(self, value):
        self._show_pv_dd = value
    @property
    def show_pv_history(self):
        return self._show_pv_history

    @show_pv_history.setter
    def show_pv_history(self, value):
        self._show_pv_history = value
    @property
    def show_uv_dd(self):
        return self._show_uv_dd

    @show_uv_dd.setter
    def show_uv_dd(self, value):
        self._show_uv_dd = value
    @property
    def show_uv_history(self):
        return self._show_uv_history

    @show_uv_history.setter
    def show_uv_history(self, value):
        self._show_uv_history = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCdpAdvertiseReportQueryResponse, self).parse_response_content(response_content)
        if 'click_pv_dd' in response:
            self.click_pv_dd = response['click_pv_dd']
        if 'click_pv_history' in response:
            self.click_pv_history = response['click_pv_history']
        if 'click_uv_dd' in response:
            self.click_uv_dd = response['click_uv_dd']
        if 'click_uv_history' in response:
            self.click_uv_history = response['click_uv_history']
        if 'report_date' in response:
            self.report_date = response['report_date']
        if 'show_pv_dd' in response:
            self.show_pv_dd = response['show_pv_dd']
        if 'show_pv_history' in response:
            self.show_pv_history = response['show_pv_history']
        if 'show_uv_dd' in response:
            self.show_uv_dd = response['show_uv_dd']
        if 'show_uv_history' in response:
            self.show_uv_history = response['show_uv_history']
