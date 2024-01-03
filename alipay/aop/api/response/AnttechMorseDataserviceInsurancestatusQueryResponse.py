#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseDataserviceInsurancestatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseDataserviceInsurancestatusQueryResponse, self).__init__()
        self._biz_no = None
        self._status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseDataserviceInsurancestatusQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'status' in response:
            self.status = response['status']
