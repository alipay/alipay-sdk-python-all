#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendDoctorScmDetail import RecommendDoctorScmDetail


class AlipayCommerceMedicalDoctorScmQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorScmQueryResponse, self).__init__()
        self._doctor_scm_list = None

    @property
    def doctor_scm_list(self):
        return self._doctor_scm_list

    @doctor_scm_list.setter
    def doctor_scm_list(self, value):
        if isinstance(value, list):
            self._doctor_scm_list = list()
            for i in value:
                if isinstance(i, RecommendDoctorScmDetail):
                    self._doctor_scm_list.append(i)
                else:
                    self._doctor_scm_list.append(RecommendDoctorScmDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorScmQueryResponse, self).parse_response_content(response_content)
        if 'doctor_scm_list' in response:
            self.doctor_scm_list = response['doctor_scm_list']
