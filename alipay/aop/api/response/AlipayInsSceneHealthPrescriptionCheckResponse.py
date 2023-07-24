#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrescriptionCheckDetail import PrescriptionCheckDetail


class AlipayInsSceneHealthPrescriptionCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneHealthPrescriptionCheckResponse, self).__init__()
        self._check_details = None
        self._check_result = None

    @property
    def check_details(self):
        return self._check_details

    @check_details.setter
    def check_details(self, value):
        if isinstance(value, list):
            self._check_details = list()
            for i in value:
                if isinstance(i, PrescriptionCheckDetail):
                    self._check_details.append(i)
                else:
                    self._check_details.append(PrescriptionCheckDetail.from_alipay_dict(i))
    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneHealthPrescriptionCheckResponse, self).parse_response_content(response_content)
        if 'check_details' in response:
            self.check_details = response['check_details']
        if 'check_result' in response:
            self.check_result = response['check_result']
