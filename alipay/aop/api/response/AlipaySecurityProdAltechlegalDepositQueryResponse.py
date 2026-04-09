#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DepositFileList import DepositFileList


class AlipaySecurityProdAltechlegalDepositQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAltechlegalDepositQueryResponse, self).__init__()
        self._deposit_file_list = None

    @property
    def deposit_file_list(self):
        return self._deposit_file_list

    @deposit_file_list.setter
    def deposit_file_list(self, value):
        if isinstance(value, list):
            self._deposit_file_list = list()
            for i in value:
                if isinstance(i, DepositFileList):
                    self._deposit_file_list.append(i)
                else:
                    self._deposit_file_list.append(DepositFileList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAltechlegalDepositQueryResponse, self).parse_response_content(response_content)
        if 'deposit_file_list' in response:
            self.deposit_file_list = response['deposit_file_list']
