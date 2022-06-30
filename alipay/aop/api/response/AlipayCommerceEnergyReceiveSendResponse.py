#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderGoodDTO import OrderGoodDTO


class AlipayCommerceEnergyReceiveSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEnergyReceiveSendResponse, self).__init__()
        self._order_good_list = None
        self._total_energy_amount = None

    @property
    def order_good_list(self):
        return self._order_good_list

    @order_good_list.setter
    def order_good_list(self, value):
        if isinstance(value, list):
            self._order_good_list = list()
            for i in value:
                if isinstance(i, OrderGoodDTO):
                    self._order_good_list.append(i)
                else:
                    self._order_good_list.append(OrderGoodDTO.from_alipay_dict(i))
    @property
    def total_energy_amount(self):
        return self._total_energy_amount

    @total_energy_amount.setter
    def total_energy_amount(self, value):
        self._total_energy_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEnergyReceiveSendResponse, self).parse_response_content(response_content)
        if 'order_good_list' in response:
            self.order_good_list = response['order_good_list']
        if 'total_energy_amount' in response:
            self.total_energy_amount = response['total_energy_amount']
