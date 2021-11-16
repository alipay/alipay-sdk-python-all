#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HealthServiceFamilyDoctorDrugDTO import HealthServiceFamilyDoctorDrugDTO


class AlipayInsSceneFamilydoctorItemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneFamilydoctorItemBatchqueryResponse, self).__init__()
        self._drugs = None

    @property
    def drugs(self):
        return self._drugs

    @drugs.setter
    def drugs(self, value):
        if isinstance(value, list):
            self._drugs = list()
            for i in value:
                if isinstance(i, HealthServiceFamilyDoctorDrugDTO):
                    self._drugs.append(i)
                else:
                    self._drugs.append(HealthServiceFamilyDoctorDrugDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneFamilydoctorItemBatchqueryResponse, self).parse_response_content(response_content)
        if 'drugs' in response:
            self.drugs = response['drugs']
