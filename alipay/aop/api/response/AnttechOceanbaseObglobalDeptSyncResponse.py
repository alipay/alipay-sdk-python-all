#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalDeptSyncResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalDeptSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalDeptSyncResponse, self).parse_response_content(response_content)
