#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxAdvancedStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxAdvancedStatusQueryResponse, self).__init__()
        self._alipay_user_id = None
        self._out_tax_refund_no = None
        self._status = None
        self._status_change_time = None
        self._status_msg = None
        self._tax_refund_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def out_tax_refund_no(self):
        return self._out_tax_refund_no

    @out_tax_refund_no.setter
    def out_tax_refund_no(self, value):
        self._out_tax_refund_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_change_time(self):
        return self._status_change_time

    @status_change_time.setter
    def status_change_time(self, value):
        self._status_change_time = value
    @property
    def status_msg(self):
        return self._status_msg

    @status_msg.setter
    def status_msg(self, value):
        self._status_msg = value
    @property
    def tax_refund_no(self):
        return self._tax_refund_no

    @tax_refund_no.setter
    def tax_refund_no(self, value):
        self._tax_refund_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxAdvancedStatusQueryResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'out_tax_refund_no' in response:
            self.out_tax_refund_no = response['out_tax_refund_no']
        if 'status' in response:
            self.status = response['status']
        if 'status_change_time' in response:
            self.status_change_time = response['status_change_time']
        if 'status_msg' in response:
            self.status_msg = response['status_msg']
        if 'tax_refund_no' in response:
            self.tax_refund_no = response['tax_refund_no']
