#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePetinsureQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePetinsureQueryResponse, self).__init__()
        self._insure_status = None

    @property
    def insure_status(self):
        return self._insure_status

    @insure_status.setter
    def insure_status(self, value):
        self._insure_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePetinsureQueryResponse, self).parse_response_content(response_content)
        if 'insure_status' in response:
            self.insure_status = response['insure_status']
