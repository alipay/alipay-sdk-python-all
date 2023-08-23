#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfSignApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfSignApplyResponse, self).__init__()
        self._out_biz_no = None
        self._process_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfSignApplyResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'process_id' in response:
            self.process_id = response['process_id']
