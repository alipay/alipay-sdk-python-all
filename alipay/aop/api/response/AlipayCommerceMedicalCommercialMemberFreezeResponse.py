#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialMemberFreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialMemberFreezeResponse, self).__init__()
        self._out_product_id = None

    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialMemberFreezeResponse, self).parse_response_content(response_content)
        if 'out_product_id' in response:
            self.out_product_id = response['out_product_id']
