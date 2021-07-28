#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductInviteStatusInfo import ProductInviteStatusInfo


class AlipayOpenInviteOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInviteOrderQueryResponse, self).__init__()
        self._merchant_pid = None
        self._sign_status_list = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def sign_status_list(self):
        return self._sign_status_list

    @sign_status_list.setter
    def sign_status_list(self, value):
        if isinstance(value, list):
            self._sign_status_list = list()
            for i in value:
                if isinstance(i, ProductInviteStatusInfo):
                    self._sign_status_list.append(i)
                else:
                    self._sign_status_list.append(ProductInviteStatusInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInviteOrderQueryResponse, self).parse_response_content(response_content)
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'sign_status_list' in response:
            self.sign_status_list = response['sign_status_list']
