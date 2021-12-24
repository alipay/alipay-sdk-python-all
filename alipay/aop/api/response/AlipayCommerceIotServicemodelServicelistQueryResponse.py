#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceServiceVO import DeviceServiceVO


class AlipayCommerceIotServicemodelServicelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotServicemodelServicelistQueryResponse, self).__init__()
        self._list = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, DeviceServiceVO):
                    self._list.append(i)
                else:
                    self._list.append(DeviceServiceVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotServicemodelServicelistQueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']