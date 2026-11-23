#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PowerInputPointDTO import PowerInputPointDTO


class DatadigitalAnttechEnergyPowerinputQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechEnergyPowerinputQueryResponse, self).__init__()
        self._data_list = None
        self._request_id = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, PowerInputPointDTO):
                    self._data_list.append(i)
                else:
                    self._data_list.append(PowerInputPointDTO.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechEnergyPowerinputQueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'request_id' in response:
            self.request_id = response['request_id']
