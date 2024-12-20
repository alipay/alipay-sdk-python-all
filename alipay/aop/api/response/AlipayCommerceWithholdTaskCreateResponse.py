#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWithholdTaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWithholdTaskCreateResponse, self).__init__()
        self._agreement_no = None
        self._out_biz_no = None
        self._withhold_no = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def withhold_no(self):
        return self._withhold_no

    @withhold_no.setter
    def withhold_no(self, value):
        self._withhold_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWithholdTaskCreateResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'withhold_no' in response:
            self.withhold_no = response['withhold_no']
