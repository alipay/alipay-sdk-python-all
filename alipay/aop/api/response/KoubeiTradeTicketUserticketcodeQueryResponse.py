#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TicketCodeQueryResponse import TicketCodeQueryResponse


class KoubeiTradeTicketUserticketcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeTicketUserticketcodeQueryResponse, self).__init__()
        self._values = None

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                if isinstance(i, TicketCodeQueryResponse):
                    self._values.append(i)
                else:
                    self._values.append(TicketCodeQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeTicketUserticketcodeQueryResponse, self).parse_response_content(response_content)
        if 'values' in response:
            self.values = response['values']
