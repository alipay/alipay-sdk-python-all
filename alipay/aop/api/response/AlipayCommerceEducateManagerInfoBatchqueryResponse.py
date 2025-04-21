#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduManagerInfo import EduManagerInfo


class AlipayCommerceEducateManagerInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateManagerInfoBatchqueryResponse, self).__init__()
        self._manager_list = None
        self._total_num = None

    @property
    def manager_list(self):
        return self._manager_list

    @manager_list.setter
    def manager_list(self, value):
        if isinstance(value, list):
            self._manager_list = list()
            for i in value:
                if isinstance(i, EduManagerInfo):
                    self._manager_list.append(i)
                else:
                    self._manager_list.append(EduManagerInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateManagerInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'manager_list' in response:
            self.manager_list = response['manager_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
