#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowCloudfundrefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowCloudfundrefundQueryResponse, self).__init__()
        self._currency = None
        self._participant_id = None
        self._participant_type = None
        self._refund_amount = None
        self._refund_biz_no = None
        self._refund_error_code = None
        self._refund_error_desc = None
        self._refund_finish_date = None
        self._refund_order_no = None
        self._refund_status = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
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
    def refund_biz_no(self):
        return self._refund_biz_no

    @refund_biz_no.setter
    def refund_biz_no(self, value):
        self._refund_biz_no = value
    @property
    def refund_error_code(self):
        return self._refund_error_code

    @refund_error_code.setter
    def refund_error_code(self, value):
        self._refund_error_code = value
    @property
    def refund_error_desc(self):
        return self._refund_error_desc

    @refund_error_desc.setter
    def refund_error_desc(self, value):
        self._refund_error_desc = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowCloudfundrefundQueryResponse, self).parse_response_content(response_content)
        if 'currency' in response:
            self.currency = response['currency']
        if 'participant_id' in response:
            self.participant_id = response['participant_id']
        if 'participant_type' in response:
            self.participant_type = response['participant_type']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_biz_no' in response:
            self.refund_biz_no = response['refund_biz_no']
        if 'refund_error_code' in response:
            self.refund_error_code = response['refund_error_code']
        if 'refund_error_desc' in response:
            self.refund_error_desc = response['refund_error_desc']
        if 'refund_finish_date' in response:
            self.refund_finish_date = response['refund_finish_date']
        if 'refund_order_no' in response:
            self.refund_order_no = response['refund_order_no']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
