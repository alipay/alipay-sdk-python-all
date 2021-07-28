#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiseaseDTO import DiseaseDTO


class AlipayInsDataDiseaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataDiseaseQueryResponse, self).__init__()
        self._disease_list = None

    @property
    def disease_list(self):
        return self._disease_list

    @disease_list.setter
    def disease_list(self, value):
        if isinstance(value, list):
            self._disease_list = list()
            for i in value:
                if isinstance(i, DiseaseDTO):
                    self._disease_list.append(i)
                else:
                    self._disease_list.append(DiseaseDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataDiseaseQueryResponse, self).parse_response_content(response_content)
        if 'disease_list' in response:
            self.disease_list = response['disease_list']
