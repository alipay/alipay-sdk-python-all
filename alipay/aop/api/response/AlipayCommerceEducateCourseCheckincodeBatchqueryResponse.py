#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduCourseCheckInRule import EduCourseCheckInRule


class AlipayCommerceEducateCourseCheckincodeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCourseCheckincodeBatchqueryResponse, self).__init__()
        self._check_in_code_list = None
        self._total_num = None

    @property
    def check_in_code_list(self):
        return self._check_in_code_list

    @check_in_code_list.setter
    def check_in_code_list(self, value):
        if isinstance(value, list):
            self._check_in_code_list = list()
            for i in value:
                if isinstance(i, EduCourseCheckInRule):
                    self._check_in_code_list.append(i)
                else:
                    self._check_in_code_list.append(EduCourseCheckInRule.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCourseCheckincodeBatchqueryResponse, self).parse_response_content(response_content)
        if 'check_in_code_list' in response:
            self.check_in_code_list = response['check_in_code_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
