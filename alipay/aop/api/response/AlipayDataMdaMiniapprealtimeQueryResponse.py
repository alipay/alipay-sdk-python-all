#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniapprealtimeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniapprealtimeQueryResponse, self).__init__()
        self._month_pv = None
        self._today_pv = None
        self._total_pv = None
        self._uv = None

    @property
    def month_pv(self):
        return self._month_pv

    @month_pv.setter
    def month_pv(self, value):
        self._month_pv = value
    @property
    def today_pv(self):
        return self._today_pv

    @today_pv.setter
    def today_pv(self, value):
        self._today_pv = value
    @property
    def total_pv(self):
        return self._total_pv

    @total_pv.setter
    def total_pv(self, value):
        self._total_pv = value
    @property
    def uv(self):
        return self._uv

    @uv.setter
    def uv(self, value):
        self._uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniapprealtimeQueryResponse, self).parse_response_content(response_content)
        if 'month_pv' in response:
            self.month_pv = response['month_pv']
        if 'today_pv' in response:
            self.today_pv = response['today_pv']
        if 'total_pv' in response:
            self.total_pv = response['total_pv']
        if 'uv' in response:
            self.uv = response['uv']
