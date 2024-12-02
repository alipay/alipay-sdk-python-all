#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataDrugorderstatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataDrugorderstatusSyncResponse, self).__init__()
        self._drug_order_id = None

    @property
    def drug_order_id(self):
        return self._drug_order_id

    @drug_order_id.setter
    def drug_order_id(self, value):
        self._drug_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataDrugorderstatusSyncResponse, self).parse_response_content(response_content)
        if 'drug_order_id' in response:
            self.drug_order_id = response['drug_order_id']
