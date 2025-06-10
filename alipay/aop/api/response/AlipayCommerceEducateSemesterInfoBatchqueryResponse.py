#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduSemesterInfo import EduSemesterInfo


class AlipayCommerceEducateSemesterInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSemesterInfoBatchqueryResponse, self).__init__()
        self._semester_list = None
        self._total_num = None

    @property
    def semester_list(self):
        return self._semester_list

    @semester_list.setter
    def semester_list(self, value):
        if isinstance(value, list):
            self._semester_list = list()
            for i in value:
                if isinstance(i, EduSemesterInfo):
                    self._semester_list.append(i)
                else:
                    self._semester_list.append(EduSemesterInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSemesterInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'semester_list' in response:
            self.semester_list = response['semester_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
