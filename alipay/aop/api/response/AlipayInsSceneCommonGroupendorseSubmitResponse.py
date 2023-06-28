#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneCommonGroupendorseSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonGroupendorseSubmitResponse, self).__init__()
        self._out_biz_no = None
        self._summary_endorse_order_no = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def summary_endorse_order_no(self):
        return self._summary_endorse_order_no

    @summary_endorse_order_no.setter
    def summary_endorse_order_no(self, value):
        self._summary_endorse_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonGroupendorseSubmitResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'summary_endorse_order_no' in response:
            self.summary_endorse_order_no = response['summary_endorse_order_no']
