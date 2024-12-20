#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnergyAggrElectricUserInfoDTO import EnergyAggrElectricUserInfoDTO


class AnttechBlockchainFinanceElectricUserBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceElectricUserBatchqueryResponse, self).__init__()
        self._electric_user_list = None
        self._total_count = None

    @property
    def electric_user_list(self):
        return self._electric_user_list

    @electric_user_list.setter
    def electric_user_list(self, value):
        if isinstance(value, list):
            self._electric_user_list = list()
            for i in value:
                if isinstance(i, EnergyAggrElectricUserInfoDTO):
                    self._electric_user_list.append(i)
                else:
                    self._electric_user_list.append(EnergyAggrElectricUserInfoDTO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceElectricUserBatchqueryResponse, self).parse_response_content(response_content)
        if 'electric_user_list' in response:
            self.electric_user_list = response['electric_user_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
