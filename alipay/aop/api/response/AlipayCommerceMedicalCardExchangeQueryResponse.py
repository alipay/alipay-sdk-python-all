#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenInfoDTO import OpenInfoDTO


class AlipayCommerceMedicalCardExchangeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCardExchangeQueryResponse, self).__init__()
        self._open_info_list = None
        self._open_status = None
        self._open_time = None

    @property
    def open_info_list(self):
        return self._open_info_list

    @open_info_list.setter
    def open_info_list(self, value):
        if isinstance(value, list):
            self._open_info_list = list()
            for i in value:
                if isinstance(i, OpenInfoDTO):
                    self._open_info_list.append(i)
                else:
                    self._open_info_list.append(OpenInfoDTO.from_alipay_dict(i))
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCardExchangeQueryResponse, self).parse_response_content(response_content)
        if 'open_info_list' in response:
            self.open_info_list = response['open_info_list']
        if 'open_status' in response:
            self.open_status = response['open_status']
        if 'open_time' in response:
            self.open_time = response['open_time']
