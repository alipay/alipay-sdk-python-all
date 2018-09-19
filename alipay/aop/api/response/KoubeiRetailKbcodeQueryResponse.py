#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RetailKbcodeQueryVo import RetailKbcodeQueryVo


class KoubeiRetailKbcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailKbcodeQueryResponse, self).__init__()
        self._code_info_list = None
        self._total_count = None

    @property
    def code_info_list(self):
        return self._code_info_list

    @code_info_list.setter
    def code_info_list(self, value):
        if isinstance(value, list):
            self._code_info_list = list()
            for i in value:
                if isinstance(i, RetailKbcodeQueryVo):
                    self._code_info_list.append(i)
                else:
                    self._code_info_list.append(RetailKbcodeQueryVo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailKbcodeQueryResponse, self).parse_response_content(response_content)
        if 'code_info_list' in response:
            self.code_info_list = response['code_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
