#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BPOpenApiTicket import BPOpenApiTicket


class AlipayBossBaseProcessTicketQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseProcessTicketQueryResponse, self).__init__()
        self._ticket = None

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        if isinstance(value, BPOpenApiTicket):
            self._ticket = value
        else:
            self._ticket = BPOpenApiTicket.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseProcessTicketQueryResponse, self).parse_response_content(response_content)
        if 'ticket' in response:
            self.ticket = response['ticket']
