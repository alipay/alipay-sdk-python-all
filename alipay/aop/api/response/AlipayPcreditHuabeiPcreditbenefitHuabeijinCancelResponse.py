#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPcreditbenefitHuabeijinCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditbenefitHuabeijinCancelResponse, self).__init__()
        self._activity_order_id = None
        self._hb_biz_code = None
        self._operation_seq_id = None
        self._out_biz_no = None

    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def hb_biz_code(self):
        return self._hb_biz_code

    @hb_biz_code.setter
    def hb_biz_code(self, value):
        self._hb_biz_code = value
    @property
    def operation_seq_id(self):
        return self._operation_seq_id

    @operation_seq_id.setter
    def operation_seq_id(self, value):
        self._operation_seq_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditbenefitHuabeijinCancelResponse, self).parse_response_content(response_content)
        if 'activity_order_id' in response:
            self.activity_order_id = response['activity_order_id']
        if 'hb_biz_code' in response:
            self.hb_biz_code = response['hb_biz_code']
        if 'operation_seq_id' in response:
            self.operation_seq_id = response['operation_seq_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
