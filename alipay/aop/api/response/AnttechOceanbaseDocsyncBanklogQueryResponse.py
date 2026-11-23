#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BankLogOpenApiDTO import BankLogOpenApiDTO


class AnttechOceanbaseDocsyncBanklogQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseDocsyncBanklogQueryResponse, self).__init__()
        self._bank_log_dto_list = None
        self._total_items = None

    @property
    def bank_log_dto_list(self):
        return self._bank_log_dto_list

    @bank_log_dto_list.setter
    def bank_log_dto_list(self, value):
        if isinstance(value, list):
            self._bank_log_dto_list = list()
            for i in value:
                if isinstance(i, BankLogOpenApiDTO):
                    self._bank_log_dto_list.append(i)
                else:
                    self._bank_log_dto_list.append(BankLogOpenApiDTO.from_alipay_dict(i))
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseDocsyncBanklogQueryResponse, self).parse_response_content(response_content)
        if 'bank_log_dto_list' in response:
            self.bank_log_dto_list = response['bank_log_dto_list']
        if 'total_items' in response:
            self.total_items = response['total_items']
