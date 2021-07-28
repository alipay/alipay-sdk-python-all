#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BindedMiniAppInfo import BindedMiniAppInfo


class AlipayOpenMiniAmpeBindedminiappBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeBindedminiappBatchqueryResponse, self).__init__()
        self._binded_mini_app_list = None
        self._total_count = None

    @property
    def binded_mini_app_list(self):
        return self._binded_mini_app_list

    @binded_mini_app_list.setter
    def binded_mini_app_list(self, value):
        if isinstance(value, list):
            self._binded_mini_app_list = list()
            for i in value:
                if isinstance(i, BindedMiniAppInfo):
                    self._binded_mini_app_list.append(i)
                else:
                    self._binded_mini_app_list.append(BindedMiniAppInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeBindedminiappBatchqueryResponse, self).parse_response_content(response_content)
        if 'binded_mini_app_list' in response:
            self.binded_mini_app_list = response['binded_mini_app_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
