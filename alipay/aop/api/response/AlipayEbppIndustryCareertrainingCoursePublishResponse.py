#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingCoursePublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingCoursePublishResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingCoursePublishResponse, self).parse_response_content(response_content)
