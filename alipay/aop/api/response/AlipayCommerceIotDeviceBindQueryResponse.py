#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotDeviceBindInfo import IotDeviceBindInfo


class AlipayCommerceIotDeviceBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceBindQueryResponse, self).__init__()
        self._bind_info_list = None

    @property
    def bind_info_list(self):
        return self._bind_info_list

    @bind_info_list.setter
    def bind_info_list(self, value):
        if isinstance(value, list):
            self._bind_info_list = list()
            for i in value:
                if isinstance(i, IotDeviceBindInfo):
                    self._bind_info_list.append(i)
                else:
                    self._bind_info_list.append(IotDeviceBindInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceBindQueryResponse, self).parse_response_content(response_content)
        if 'bind_info_list' in response:
            self.bind_info_list = response['bind_info_list']
