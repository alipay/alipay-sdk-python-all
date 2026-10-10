#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPcreditbenefitHuabeijinRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditbenefitHuabeijinRefundResponse, self).__init__()
        self._activity_order_id = None
        self._actual_deducted = None
        self._hb_biz_code = None
        self._operation_seq_id = None
        self._out_biz_no = None
        self._should_deducted = None

    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def actual_deducted(self):
        return self._actual_deducted

    @actual_deducted.setter
    def actual_deducted(self, value):
        self._actual_deducted = value
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
    @property
    def should_deducted(self):
        return self._should_deducted

    @should_deducted.setter
    def should_deducted(self, value):
        self._should_deducted = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditbenefitHuabeijinRefundResponse, self).parse_response_content(response_content)
        if 'activity_order_id' in response:
            self.activity_order_id = response['activity_order_id']
        if 'actual_deducted' in response:
            self.actual_deducted = response['actual_deducted']
        if 'hb_biz_code' in response:
            self.hb_biz_code = response['hb_biz_code']
        if 'operation_seq_id' in response:
            self.operation_seq_id = response['operation_seq_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'should_deducted' in response:
            self.should_deducted = response['should_deducted']
