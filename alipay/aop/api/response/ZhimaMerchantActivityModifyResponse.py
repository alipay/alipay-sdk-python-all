#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantActivityModifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantActivityModifyResponse, self).__init__()
        self._activity_no = None

    @property
    def activity_no(self):
        return self._activity_no

    @activity_no.setter
    def activity_no(self, value):
        self._activity_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantActivityModifyResponse, self).parse_response_content(response_content)
        if 'activity_no' in response:
            self.activity_no = response['activity_no']
