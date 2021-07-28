#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserFamilyShareAdmittancePreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFamilyShareAdmittancePreconsultResponse, self).__init__()
        self._admittance = None
        self._unadmitted_reason = None

    @property
    def admittance(self):
        return self._admittance

    @admittance.setter
    def admittance(self, value):
        self._admittance = value
    @property
    def unadmitted_reason(self):
        return self._unadmitted_reason

    @unadmitted_reason.setter
    def unadmitted_reason(self, value):
        self._unadmitted_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserFamilyShareAdmittancePreconsultResponse, self).parse_response_content(response_content)
        if 'admittance' in response:
            self.admittance = response['admittance']
        if 'unadmitted_reason' in response:
            self.unadmitted_reason = response['unadmitted_reason']
