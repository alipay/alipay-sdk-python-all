#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpecialtyDiseasePackage import SpecialtyDiseasePackage


class AlipayCommerceMedicalServicepackageListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageListQueryResponse, self).__init__()
        self._specialty_disease_package_list = None

    @property
    def specialty_disease_package_list(self):
        return self._specialty_disease_package_list

    @specialty_disease_package_list.setter
    def specialty_disease_package_list(self, value):
        if isinstance(value, list):
            self._specialty_disease_package_list = list()
            for i in value:
                if isinstance(i, SpecialtyDiseasePackage):
                    self._specialty_disease_package_list.append(i)
                else:
                    self._specialty_disease_package_list.append(SpecialtyDiseasePackage.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageListQueryResponse, self).parse_response_content(response_content)
        if 'specialty_disease_package_list' in response:
            self.specialty_disease_package_list = response['specialty_disease_package_list']
