#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendDoctorDetail import RecommendDoctorDetail


class AlipayCommerceMedicalDoctorRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorRecommendQueryResponse, self).__init__()
        self._hdf_doctor_list = None

    @property
    def hdf_doctor_list(self):
        return self._hdf_doctor_list

    @hdf_doctor_list.setter
    def hdf_doctor_list(self, value):
        if isinstance(value, list):
            self._hdf_doctor_list = list()
            for i in value:
                if isinstance(i, RecommendDoctorDetail):
                    self._hdf_doctor_list.append(i)
                else:
                    self._hdf_doctor_list.append(RecommendDoctorDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorRecommendQueryResponse, self).parse_response_content(response_content)
        if 'hdf_doctor_list' in response:
            self.hdf_doctor_list = response['hdf_doctor_list']
