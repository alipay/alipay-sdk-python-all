#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceEnterpriseinvoiceReissueCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseinvoiceReissueCreateResponse, self).__init__()
        self._apply_flow_id = None
        self._apply_status = None

    @property
    def apply_flow_id(self):
        return self._apply_flow_id

    @apply_flow_id.setter
    def apply_flow_id(self, value):
        self._apply_flow_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseinvoiceReissueCreateResponse, self).parse_response_content(response_content)
        if 'apply_flow_id' in response:
            self.apply_flow_id = response['apply_flow_id']
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
