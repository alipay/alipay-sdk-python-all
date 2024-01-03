#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderInstallmentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderInstallmentCreateResponse, self).__init__()
        self._installment_order_id = None

    @property
    def installment_order_id(self):
        return self._installment_order_id

    @installment_order_id.setter
    def installment_order_id(self, value):
        self._installment_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderInstallmentCreateResponse, self).parse_response_content(response_content)
        if 'installment_order_id' in response:
            self.installment_order_id = response['installment_order_id']
