#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduCourseInfo import EduCourseInfo


class AlipayCommerceEducateCourseInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCourseInfoBatchqueryResponse, self).__init__()
        self._course_list = None
        self._total_num = None

    @property
    def course_list(self):
        return self._course_list

    @course_list.setter
    def course_list(self, value):
        if isinstance(value, list):
            self._course_list = list()
            for i in value:
                if isinstance(i, EduCourseInfo):
                    self._course_list.append(i)
                else:
                    self._course_list.append(EduCourseInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCourseInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'course_list' in response:
            self.course_list = response['course_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
