#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupervisionOrderTransferBillInfo import SupervisionOrderTransferBillInfo


class AlipayEbppIndustrySupervisionTransferbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionTransferbillQueryResponse, self).__init__()
        self._transfer_bill_list = None

    @property
    def transfer_bill_list(self):
        return self._transfer_bill_list

    @transfer_bill_list.setter
    def transfer_bill_list(self, value):
        if isinstance(value, list):
            self._transfer_bill_list = list()
            for i in value:
                if isinstance(i, SupervisionOrderTransferBillInfo):
                    self._transfer_bill_list.append(i)
                else:
                    self._transfer_bill_list.append(SupervisionOrderTransferBillInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionTransferbillQueryResponse, self).parse_response_content(response_content)
        if 'transfer_bill_list' in response:
            self.transfer_bill_list = response['transfer_bill_list']
