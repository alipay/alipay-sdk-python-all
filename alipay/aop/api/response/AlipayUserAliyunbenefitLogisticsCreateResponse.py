#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAliyunbenefitLogisticsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAliyunbenefitLogisticsCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserAliyunbenefitLogisticsCreateResponse, self).parse_response_content(response_content)
