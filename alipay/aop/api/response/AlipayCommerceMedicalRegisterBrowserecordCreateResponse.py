#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterBrowserecordCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterBrowserecordCreateResponse, self).__init__()
        self._res_prop = None

    @property
    def res_prop(self):
        return self._res_prop

    @res_prop.setter
    def res_prop(self, value):
        self._res_prop = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterBrowserecordCreateResponse, self).parse_response_content(response_content)
        if 'res_prop' in response:
            self.res_prop = response['res_prop']
