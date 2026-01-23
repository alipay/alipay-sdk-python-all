#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentPayQueryBillInfoResponse import RentPayQueryBillInfoResponse


class AlipayEbppIndustryRentBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentBillQueryResponse, self).__init__()
        self._user_bill_list = None

    @property
    def user_bill_list(self):
        return self._user_bill_list

    @user_bill_list.setter
    def user_bill_list(self, value):
        if isinstance(value, list):
            self._user_bill_list = list()
            for i in value:
                if isinstance(i, RentPayQueryBillInfoResponse):
                    self._user_bill_list.append(i)
                else:
                    self._user_bill_list.append(RentPayQueryBillInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentBillQueryResponse, self).parse_response_content(response_content)
        if 'user_bill_list' in response:
            self.user_bill_list = response['user_bill_list']
