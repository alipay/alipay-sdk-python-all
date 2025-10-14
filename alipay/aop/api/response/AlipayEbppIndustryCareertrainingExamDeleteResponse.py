#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingExamDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingExamDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingExamDeleteResponse, self).parse_response_content(response_content)
