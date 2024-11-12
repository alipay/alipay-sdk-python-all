#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalCloudfeereductionModifyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalCloudfeereductionModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalCloudfeereductionModifyResponse, self).parse_response_content(response_content)
