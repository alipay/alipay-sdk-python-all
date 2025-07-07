#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnergyForecastInfo import EnergyForecastInfo


class DatadigitalAnttechLoadForecastQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechLoadForecastQueryResponse, self).__init__()
        self._data = None
        self._quota_cost = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, EnergyForecastInfo):
                    self._data.append(i)
                else:
                    self._data.append(EnergyForecastInfo.from_alipay_dict(i))
    @property
    def quota_cost(self):
        return self._quota_cost

    @quota_cost.setter
    def quota_cost(self, value):
        self._quota_cost = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechLoadForecastQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'quota_cost' in response:
            self.quota_cost = response['quota_cost']
