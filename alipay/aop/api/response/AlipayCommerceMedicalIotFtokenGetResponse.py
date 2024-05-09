#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIotFtokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIotFtokenGetResponse, self).__init__()
        self._fm_flag = None
        self._ftoken = None

    @property
    def fm_flag(self):
        return self._fm_flag

    @fm_flag.setter
    def fm_flag(self, value):
        self._fm_flag = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIotFtokenGetResponse, self).parse_response_content(response_content)
        if 'fm_flag' in response:
            self.fm_flag = response['fm_flag']
        if 'ftoken' in response:
            self.ftoken = response['ftoken']
