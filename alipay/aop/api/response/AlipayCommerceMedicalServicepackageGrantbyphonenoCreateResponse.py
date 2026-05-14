#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServicepackageGrantbyphonenoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServicepackageGrantbyphonenoCreateResponse, self).__init__()
        self._unique_biz_no = None

    @property
    def unique_biz_no(self):
        return self._unique_biz_no

    @unique_biz_no.setter
    def unique_biz_no(self, value):
        self._unique_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServicepackageGrantbyphonenoCreateResponse, self).parse_response_content(response_content)
        if 'unique_biz_no' in response:
            self.unique_biz_no = response['unique_biz_no']
