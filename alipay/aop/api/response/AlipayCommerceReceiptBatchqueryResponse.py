#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReceiptEnergyInfoDTO import ReceiptEnergyInfoDTO


class AlipayCommerceReceiptBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceReceiptBatchqueryResponse, self).__init__()
        self._receipt_energy_infos = None

    @property
    def receipt_energy_infos(self):
        return self._receipt_energy_infos

    @receipt_energy_infos.setter
    def receipt_energy_infos(self, value):
        if isinstance(value, list):
            self._receipt_energy_infos = list()
            for i in value:
                if isinstance(i, ReceiptEnergyInfoDTO):
                    self._receipt_energy_infos.append(i)
                else:
                    self._receipt_energy_infos.append(ReceiptEnergyInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceReceiptBatchqueryResponse, self).parse_response_content(response_content)
        if 'receipt_energy_infos' in response:
            self.receipt_energy_infos = response['receipt_energy_infos']
