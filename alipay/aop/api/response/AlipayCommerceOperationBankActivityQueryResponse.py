#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BankActivityInfo import BankActivityInfo


class AlipayCommerceOperationBankActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBankActivityQueryResponse, self).__init__()
        self._activity_info_list = None
        self._merchant_tag = None

    @property
    def activity_info_list(self):
        return self._activity_info_list

    @activity_info_list.setter
    def activity_info_list(self, value):
        if isinstance(value, list):
            self._activity_info_list = list()
            for i in value:
                if isinstance(i, BankActivityInfo):
                    self._activity_info_list.append(i)
                else:
                    self._activity_info_list.append(BankActivityInfo.from_alipay_dict(i))
    @property
    def merchant_tag(self):
        return self._merchant_tag

    @merchant_tag.setter
    def merchant_tag(self, value):
        self._merchant_tag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBankActivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_info_list' in response:
            self.activity_info_list = response['activity_info_list']
        if 'merchant_tag' in response:
            self.merchant_tag = response['merchant_tag']
