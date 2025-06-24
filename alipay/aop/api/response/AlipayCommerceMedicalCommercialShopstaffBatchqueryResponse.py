#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DentalArchivesShopStaff import DentalArchivesShopStaff


class AlipayCommerceMedicalCommercialShopstaffBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialShopstaffBatchqueryResponse, self).__init__()
        self._staffs = None

    @property
    def staffs(self):
        return self._staffs

    @staffs.setter
    def staffs(self, value):
        if isinstance(value, list):
            self._staffs = list()
            for i in value:
                if isinstance(i, DentalArchivesShopStaff):
                    self._staffs.append(i)
                else:
                    self._staffs.append(DentalArchivesShopStaff.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialShopstaffBatchqueryResponse, self).parse_response_content(response_content)
        if 'staffs' in response:
            self.staffs = response['staffs']
