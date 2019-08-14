#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiSalesLeadsSaleleadsCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesLeadsSaleleadsCreateResponse, self).__init__()
        self._leads_id = None

    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesLeadsSaleleadsCreateResponse, self).parse_response_content(response_content)
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
