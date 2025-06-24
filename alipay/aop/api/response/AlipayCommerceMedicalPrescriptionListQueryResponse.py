#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrscVO import PrscVO


class AlipayCommerceMedicalPrescriptionListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPrescriptionListQueryResponse, self).__init__()
        self._prsc_list = None

    @property
    def prsc_list(self):
        return self._prsc_list

    @prsc_list.setter
    def prsc_list(self, value):
        if isinstance(value, list):
            self._prsc_list = list()
            for i in value:
                if isinstance(i, PrscVO):
                    self._prsc_list.append(i)
                else:
                    self._prsc_list.append(PrscVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPrescriptionListQueryResponse, self).parse_response_content(response_content)
        if 'prsc_list' in response:
            self.prsc_list = response['prsc_list']
