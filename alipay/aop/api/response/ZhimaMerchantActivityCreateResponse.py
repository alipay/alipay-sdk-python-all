#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantActivityCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantActivityCreateResponse, self).__init__()
        self._activity_no = None
        self._out_activity_no = None

    @property
    def activity_no(self):
        return self._activity_no

    @activity_no.setter
    def activity_no(self, value):
        self._activity_no = value
    @property
    def out_activity_no(self):
        return self._out_activity_no

    @out_activity_no.setter
    def out_activity_no(self, value):
        self._out_activity_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantActivityCreateResponse, self).parse_response_content(response_content)
        if 'activity_no' in response:
            self.activity_no = response['activity_no']
        if 'out_activity_no' in response:
            self.out_activity_no = response['out_activity_no']
