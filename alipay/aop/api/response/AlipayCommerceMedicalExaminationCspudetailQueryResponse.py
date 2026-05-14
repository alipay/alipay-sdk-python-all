#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExaminationSpuInfo import ExaminationSpuInfo


class AlipayCommerceMedicalExaminationCspudetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalExaminationCspudetailQueryResponse, self).__init__()
        self._spu_info_list = None

    @property
    def spu_info_list(self):
        return self._spu_info_list

    @spu_info_list.setter
    def spu_info_list(self, value):
        if isinstance(value, list):
            self._spu_info_list = list()
            for i in value:
                if isinstance(i, ExaminationSpuInfo):
                    self._spu_info_list.append(i)
                else:
                    self._spu_info_list.append(ExaminationSpuInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalExaminationCspudetailQueryResponse, self).parse_response_content(response_content)
        if 'spu_info_list' in response:
            self.spu_info_list = response['spu_info_list']
