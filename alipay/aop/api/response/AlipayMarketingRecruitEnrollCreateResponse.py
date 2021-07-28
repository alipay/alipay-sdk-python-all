#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingRecruitEnrollCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingRecruitEnrollCreateResponse, self).__init__()
        self._enroll_id = None
        self._out_biz_no = None

    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingRecruitEnrollCreateResponse, self).parse_response_content(response_content)
        if 'enroll_id' in response:
            self.enroll_id = response['enroll_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
