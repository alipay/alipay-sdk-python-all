#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySupervisionOrderfundTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySupervisionOrderfundTransferResponse, self).__init__()
        self._operate_no = None

    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySupervisionOrderfundTransferResponse, self).parse_response_content(response_content)
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
