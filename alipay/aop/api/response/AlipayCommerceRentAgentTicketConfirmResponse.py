#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsultDetail import ConsultDetail


class AlipayCommerceRentAgentTicketConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentAgentTicketConfirmResponse, self).__init__()
        self._consult_detail = None

    @property
    def consult_detail(self):
        return self._consult_detail

    @consult_detail.setter
    def consult_detail(self, value):
        if isinstance(value, ConsultDetail):
            self._consult_detail = value
        else:
            self._consult_detail = ConsultDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentAgentTicketConfirmResponse, self).parse_response_content(response_content)
        if 'consult_detail' in response:
            self.consult_detail = response['consult_detail']
