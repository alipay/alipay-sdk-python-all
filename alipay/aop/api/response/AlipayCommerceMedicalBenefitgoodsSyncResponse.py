#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalBenefitgoodsSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalBenefitgoodsSyncResponse, self).__init__()
        self._sync_result = None

    @property
    def sync_result(self):
        return self._sync_result

    @sync_result.setter
    def sync_result(self, value):
        self._sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalBenefitgoodsSyncResponse, self).parse_response_content(response_content)
        if 'sync_result' in response:
            self.sync_result = response['sync_result']
