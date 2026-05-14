#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RightsResult import RightsResult


class AlipayCommerceMedicalServiceRightsCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceRightsCheckResponse, self).__init__()
        self._rights_result = None

    @property
    def rights_result(self):
        return self._rights_result

    @rights_result.setter
    def rights_result(self, value):
        if isinstance(value, RightsResult):
            self._rights_result = value
        else:
            self._rights_result = RightsResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceRightsCheckResponse, self).parse_response_content(response_content)
        if 'rights_result' in response:
            self.rights_result = response['rights_result']
