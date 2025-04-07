#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentLoanConsultResult import RentLoanConsultResult


class AlipayCommerceRentLoanConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentLoanConsultResponse, self).__init__()
        self._consult_result_infos = None

    @property
    def consult_result_infos(self):
        return self._consult_result_infos

    @consult_result_infos.setter
    def consult_result_infos(self, value):
        if isinstance(value, list):
            self._consult_result_infos = list()
            for i in value:
                if isinstance(i, RentLoanConsultResult):
                    self._consult_result_infos.append(i)
                else:
                    self._consult_result_infos.append(RentLoanConsultResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentLoanConsultResponse, self).parse_response_content(response_content)
        if 'consult_result_infos' in response:
            self.consult_result_infos = response['consult_result_infos']
