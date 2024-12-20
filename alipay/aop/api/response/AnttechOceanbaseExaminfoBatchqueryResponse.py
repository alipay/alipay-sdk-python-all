#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExamInfoDTO import ExamInfoDTO


class AnttechOceanbaseExaminfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseExaminfoBatchqueryResponse, self).__init__()
        self._exam_infos = None

    @property
    def exam_infos(self):
        return self._exam_infos

    @exam_infos.setter
    def exam_infos(self, value):
        if isinstance(value, list):
            self._exam_infos = list()
            for i in value:
                if isinstance(i, ExamInfoDTO):
                    self._exam_infos.append(i)
                else:
                    self._exam_infos.append(ExamInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseExaminfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'exam_infos' in response:
            self.exam_infos = response['exam_infos']
