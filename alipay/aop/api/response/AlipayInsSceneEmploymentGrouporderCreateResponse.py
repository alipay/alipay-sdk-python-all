#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneEmploymentGrouporderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEmploymentGrouporderCreateResponse, self).__init__()
        self._out_biz_no = None
        self._summary_order_no = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def summary_order_no(self):
        return self._summary_order_no

    @summary_order_no.setter
    def summary_order_no(self, value):
        self._summary_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEmploymentGrouporderCreateResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'summary_order_no' in response:
            self.summary_order_no = response['summary_order_no']
