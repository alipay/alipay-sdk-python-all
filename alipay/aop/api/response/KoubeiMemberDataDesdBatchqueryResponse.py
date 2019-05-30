#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GavintestNewonline import GavintestNewonline


class KoubeiMemberDataDesdBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMemberDataDesdBatchqueryResponse, self).__init__()
        self._de = None

    @property
    def de(self):
        return self._de

    @de.setter
    def de(self, value):
        if isinstance(value, GavintestNewonline):
            self._de = value
        else:
            self._de = GavintestNewonline.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMemberDataDesdBatchqueryResponse, self).parse_response_content(response_content)
        if 'de' in response:
            self.de = response['de']
