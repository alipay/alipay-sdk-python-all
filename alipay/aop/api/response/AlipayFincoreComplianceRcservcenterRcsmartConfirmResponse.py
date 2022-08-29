#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RcSmartResponse import RcSmartResponse


class AlipayFincoreComplianceRcservcenterRcsmartConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceRcservcenterRcsmartConfirmResponse, self).__init__()
        self._rc_smart_response = None

    @property
    def rc_smart_response(self):
        return self._rc_smart_response

    @rc_smart_response.setter
    def rc_smart_response(self, value):
        if isinstance(value, RcSmartResponse):
            self._rc_smart_response = value
        else:
            self._rc_smart_response = RcSmartResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceRcservcenterRcsmartConfirmResponse, self).parse_response_content(response_content)
        if 'rc_smart_response' in response:
            self.rc_smart_response = response['rc_smart_response']
