#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryRefundQueryResponse, self).__init__()
        self._bank_error_code = None
        self._bank_error_desc = None
        self._channel_refund_order_no = None
        self._currency = None
        self._ext_info = None
        self._memo = None
        self._out_refund_no = None
        self._participant_actual_refund_amount = None
        self._participant_id = None
        self._participant_type = None
        self._refund_amount = None
        self._refund_finish_date = None
        self._refund_order_no = None
        self._refund_status = None
        self._relate_order_no = None
        self._sign_xml = None

    @property
    def bank_error_code(self):
        return self._bank_error_code

    @bank_error_code.setter
    def bank_error_code(self, value):
        self._bank_error_code = value
    @property
    def bank_error_desc(self):
        return self._bank_error_desc

    @bank_error_desc.setter
    def bank_error_desc(self, value):
        self._bank_error_desc = value
    @property
    def channel_refund_order_no(self):
        return self._channel_refund_order_no

    @channel_refund_order_no.setter
    def channel_refund_order_no(self, value):
        self._channel_refund_order_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def participant_actual_refund_amount(self):
        return self._participant_actual_refund_amount

    @participant_actual_refund_amount.setter
    def participant_actual_refund_amount(self, value):
        self._participant_actual_refund_amount = value
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
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_finish_date(self):
        return self._refund_finish_date

    @refund_finish_date.setter
    def refund_finish_date(self, value):
        self._refund_finish_date = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
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
        response = super(AlipayEbppIndustrySalaryRefundQueryResponse, self).parse_response_content(response_content)
        if 'bank_error_code' in response:
            self.bank_error_code = response['bank_error_code']
        if 'bank_error_desc' in response:
            self.bank_error_desc = response['bank_error_desc']
        if 'channel_refund_order_no' in response:
            self.channel_refund_order_no = response['channel_refund_order_no']
        if 'currency' in response:
            self.currency = response['currency']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'memo' in response:
            self.memo = response['memo']
        if 'out_refund_no' in response:
            self.out_refund_no = response['out_refund_no']
        if 'participant_actual_refund_amount' in response:
            self.participant_actual_refund_amount = response['participant_actual_refund_amount']
        if 'participant_id' in response:
            self.participant_id = response['participant_id']
        if 'participant_type' in response:
            self.participant_type = response['participant_type']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_finish_date' in response:
            self.refund_finish_date = response['refund_finish_date']
        if 'refund_order_no' in response:
            self.refund_order_no = response['refund_order_no']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'relate_order_no' in response:
            self.relate_order_no = response['relate_order_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
