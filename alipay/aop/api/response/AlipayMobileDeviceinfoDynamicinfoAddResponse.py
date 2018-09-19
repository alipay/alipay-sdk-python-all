#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileDeviceinfoDynamicinfoAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileDeviceinfoDynamicinfoAddResponse, self).__init__()
        self._operateresult = None

    @property
    def operateresult(self):
        return self._operateresult

    @operateresult.setter
    def operateresult(self, value):
        self._operateresult = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileDeviceinfoDynamicinfoAddResponse, self).parse_response_content(response_content)
        if 'operateresult' in response:
            self.operateresult = response['operateresult']
