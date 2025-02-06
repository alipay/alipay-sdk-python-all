#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryRefundApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryRefundApplyResponse, self).__init__()
        self._out_refund_no = None
        self._participant_id = None
        self._participant_type = None
        self._refund_order_no = None
        self._relate_order_no = None
        self._sign_xml = None

    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def participant_type(self):
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        self._participant_type = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value
    @property
    def relate_order_no(self):
        return self._relate_order_no

    @relate_order_no.setter
    def relate_order_no(self, value):
        self._relate_order_no = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryRefundApplyResponse, self).parse_response_content(response_content)
        if 'out_refund_no' in response:
            self.out_refund_no = response['out_refund_no']
        if 'participant_id' in response:
            self.participant_id = response['participant_id']
        if 'participant_type' in response:
            self.participant_type = response['participant_type']
        if 'refund_order_no' in response:
            self.refund_order_no = response['refund_order_no']
        if 'relate_order_no' in response:
            self.relate_order_no = response['relate_order_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
