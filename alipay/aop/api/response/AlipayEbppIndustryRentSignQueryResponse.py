#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentPayQueryUserSignInfoResponse import RentPayQueryUserSignInfoResponse


class AlipayEbppIndustryRentSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentSignQueryResponse, self).__init__()
        self._sign_info_list = None

    @property
    def sign_info_list(self):
        return self._sign_info_list

    @sign_info_list.setter
    def sign_info_list(self, value):
        if isinstance(value, list):
            self._sign_info_list = list()
            for i in value:
                if isinstance(i, RentPayQueryUserSignInfoResponse):
                    self._sign_info_list.append(i)
                else:
                    self._sign_info_list.append(RentPayQueryUserSignInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentSignQueryResponse, self).parse_response_content(response_content)
        if 'sign_info_list' in response:
            self.sign_info_list = response['sign_info_list']
