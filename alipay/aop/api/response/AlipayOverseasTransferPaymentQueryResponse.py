#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferPaymentQueryResponse, self).__init__()
        self._additional_beneficiary_details = None
        self._instructed_amount_type = None
        self._pass_through_info = None
        self._transfer_from_amount = None
        self._transfer_id = None
        self._transfer_result = None
        self._transfer_time = None
        self._transfer_to_amount = None

    @property
    def additional_beneficiary_details(self):
        return self._additional_beneficiary_details

    @additional_beneficiary_details.setter
    def additional_beneficiary_details(self, value):
        self._additional_beneficiary_details = value
    @property
    def instructed_amount_type(self):
        return self._instructed_amount_type

    @instructed_amount_type.setter
    def instructed_amount_type(self, value):
        self._instructed_amount_type = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def transfer_from_amount(self):
        return self._transfer_from_amount

    @transfer_from_amount.setter
    def transfer_from_amount(self, value):
        self._transfer_from_amount = value
    @property
    def transfer_id(self):
        return self._transfer_id

    @transfer_id.setter
    def transfer_id(self, value):
        self._transfer_id = value
    @property
    def transfer_result(self):
        return self._transfer_result

    @transfer_result.setter
    def transfer_result(self, value):
        self._transfer_result = value
    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value
    @property
    def transfer_to_amount(self):
        return self._transfer_to_amount

    @transfer_to_amount.setter
    def transfer_to_amount(self, value):
        self._transfer_to_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferPaymentQueryResponse, self).parse_response_content(response_content)
        if 'additional_beneficiary_details' in response:
            self.additional_beneficiary_details = response['additional_beneficiary_details']
        if 'instructed_amount_type' in response:
            self.instructed_amount_type = response['instructed_amount_type']
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
        if 'transfer_from_amount' in response:
            self.transfer_from_amount = response['transfer_from_amount']
        if 'transfer_id' in response:
            self.transfer_id = response['transfer_id']
        if 'transfer_result' in response:
            self.transfer_result = response['transfer_result']
        if 'transfer_time' in response:
            self.transfer_time = response['transfer_time']
        if 'transfer_to_amount' in response:
            self.transfer_to_amount = response['transfer_to_amount']
