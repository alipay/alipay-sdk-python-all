#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PlatformRegisterOrderList import PlatformRegisterOrderList


class AlipayCommerceMedicalRegisterLatestorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterLatestorderQueryResponse, self).__init__()
        self._order_list_url = None
        self._register_order_list = None

    @property
    def order_list_url(self):
        return self._order_list_url

    @order_list_url.setter
    def order_list_url(self, value):
        self._order_list_url = value
    @property
    def register_order_list(self):
        return self._register_order_list

    @register_order_list.setter
    def register_order_list(self, value):
        if isinstance(value, list):
            self._register_order_list = list()
            for i in value:
                if isinstance(i, PlatformRegisterOrderList):
                    self._register_order_list.append(i)
                else:
                    self._register_order_list.append(PlatformRegisterOrderList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterLatestorderQueryResponse, self).parse_response_content(response_content)
        if 'order_list_url' in response:
            self.order_list_url = response['order_list_url']
        if 'register_order_list' in response:
            self.register_order_list = response['register_order_list']
