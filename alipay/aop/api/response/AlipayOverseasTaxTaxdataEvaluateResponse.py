#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaxUserDto import TaxUserDto
from alipay.aop.api.domain.TaxUserDto import TaxUserDto


class AlipayOverseasTaxTaxdataEvaluateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxTaxdataEvaluateResponse, self).__init__()
        self._payee = None
        self._payees = None

    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        if isinstance(value, TaxUserDto):
            self._payee = value
        else:
            self._payee = TaxUserDto.from_alipay_dict(value)
    @property
    def payees(self):
        return self._payees

    @payees.setter
    def payees(self, value):
        if isinstance(value, list):
            self._payees = list()
            for i in value:
                if isinstance(i, TaxUserDto):
                    self._payees.append(i)
                else:
                    self._payees.append(TaxUserDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxTaxdataEvaluateResponse, self).parse_response_content(response_content)
        if 'payee' in response:
            self.payee = response['payee']
        if 'payees' in response:
            self.payees = response['payees']
