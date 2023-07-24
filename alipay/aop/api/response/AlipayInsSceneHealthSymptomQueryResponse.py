#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HealthSymptom import HealthSymptom


class AlipayInsSceneHealthSymptomQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneHealthSymptomQueryResponse, self).__init__()
        self._symptom_list = None

    @property
    def symptom_list(self):
        return self._symptom_list

    @symptom_list.setter
    def symptom_list(self, value):
        if isinstance(value, list):
            self._symptom_list = list()
            for i in value:
                if isinstance(i, HealthSymptom):
                    self._symptom_list.append(i)
                else:
                    self._symptom_list.append(HealthSymptom.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneHealthSymptomQueryResponse, self).parse_response_content(response_content)
        if 'symptom_list' in response:
            self.symptom_list = response['symptom_list']
