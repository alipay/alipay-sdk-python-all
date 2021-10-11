#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateBusinessServiceApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateBusinessServiceApplyResponse, self).__init__()
        self._school_no = None

    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateBusinessServiceApplyResponse, self).parse_response_content(response_content)
        if 'school_no' in response:
            self.school_no = response['school_no']
