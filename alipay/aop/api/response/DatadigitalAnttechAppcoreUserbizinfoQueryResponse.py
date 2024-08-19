#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechAppcoreUserbizinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechAppcoreUserbizinfoQueryResponse, self).__init__()
        self._heat_data = None
        self._heat_list = None

    @property
    def heat_data(self):
        return self._heat_data

    @heat_data.setter
    def heat_data(self, value):
        self._heat_data = value
    @property
    def heat_list(self):
        return self._heat_list

    @heat_list.setter
    def heat_list(self, value):
        self._heat_list = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechAppcoreUserbizinfoQueryResponse, self).parse_response_content(response_content)
        if 'heat_data' in response:
            self.heat_data = response['heat_data']
        if 'heat_list' in response:
            self.heat_list = response['heat_list']
