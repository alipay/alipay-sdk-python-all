#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceTechnicianDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceTechnicianDeleteResponse, self).__init__()
        self._technician_id = None

    @property
    def technician_id(self):
        return self._technician_id

    @technician_id.setter
    def technician_id(self, value):
        self._technician_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceTechnicianDeleteResponse, self).parse_response_content(response_content)
        if 'technician_id' in response:
            self.technician_id = response['technician_id']
