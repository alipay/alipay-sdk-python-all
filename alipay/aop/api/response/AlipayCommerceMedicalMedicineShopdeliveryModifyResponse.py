#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMedicineShopdeliveryModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedicineShopdeliveryModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedicineShopdeliveryModifyResponse, self).parse_response_content(response_content)
