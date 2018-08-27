#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CPAliveBillEntrySet import CPAliveBillEntrySet


class AlipayEcoCplifeBillModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeBillModifyResponse, self).__init__()
        self._alive_bill_entry_list = None

    @property
    def alive_bill_entry_list(self):
        return self._alive_bill_entry_list

    @alive_bill_entry_list.setter
    def alive_bill_entry_list(self, value):
        if isinstance(value, list):
            self._alive_bill_entry_list = list()
            for i in value:
                if isinstance(i, CPAliveBillEntrySet):
                    self._alive_bill_entry_list.append(i)
                else:
                    self._alive_bill_entry_list.append(CPAliveBillEntrySet.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeBillModifyResponse, self).parse_response_content(response_content)
        if 'alive_bill_entry_list' in response:
            self.alive_bill_entry_list = response['alive_bill_entry_list']
