#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrescriptionInfo import PrescriptionInfo


class AlipayCommerceMedicalHmPrescriptionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmPrescriptionQueryResponse, self).__init__()
        self._prescription_infos = None

    @property
    def prescription_infos(self):
        return self._prescription_infos

    @prescription_infos.setter
    def prescription_infos(self, value):
        if isinstance(value, list):
            self._prescription_infos = list()
            for i in value:
                if isinstance(i, PrescriptionInfo):
                    self._prescription_infos.append(i)
                else:
                    self._prescription_infos.append(PrescriptionInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmPrescriptionQueryResponse, self).parse_response_content(response_content)
        if 'prescription_infos' in response:
            self.prescription_infos = response['prescription_infos']
