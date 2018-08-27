#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TicketDetailInfo import TicketDetailInfo


class AlipayCommerceCityfacilitatorVoucherBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorVoucherBatchqueryResponse, self).__init__()
        self._tickets = None

    @property
    def tickets(self):
        return self._tickets

    @tickets.setter
    def tickets(self, value):
        if isinstance(value, list):
            self._tickets = list()
            for i in value:
                if isinstance(i, TicketDetailInfo):
                    self._tickets.append(i)
                else:
                    self._tickets.append(TicketDetailInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorVoucherBatchqueryResponse, self).parse_response_content(response_content)
        if 'tickets' in response:
            self.tickets = response['tickets']
