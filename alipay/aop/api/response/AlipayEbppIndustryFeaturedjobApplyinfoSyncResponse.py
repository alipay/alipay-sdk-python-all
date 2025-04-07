#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryFeaturedjobApplyinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryFeaturedjobApplyinfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryFeaturedjobApplyinfoSyncResponse, self).parse_response_content(response_content)
