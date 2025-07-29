#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountrefundApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountrefundApplyResponse, self).__init__()
        self._accepted_refund = None

    @property
    def accepted_refund(self):
        return self._accepted_refund

    @accepted_refund.setter
    def accepted_refund(self, value):
        self._accepted_refund = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountrefundApplyResponse, self).parse_response_content(response_content)
        if 'accepted_refund' in response:
            self.accepted_refund = response['accepted_refund']
