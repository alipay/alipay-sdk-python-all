#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GrantBankCard import GrantBankCard


class AlipayPcreditLoanSideloanlendElementConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanlendElementConsultResponse, self).__init__()
        self._admit = None
        self._default_bank_card = None
        self._extension = None
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._repayment_method_and_term_map = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._un_limit_url = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def default_bank_card(self):
        return self._default_bank_card

    @default_bank_card.setter
    def default_bank_card(self, value):
        if isinstance(value, GrantBankCard):
            self._default_bank_card = value
        else:
            self._default_bank_card = GrantBankCard.from_alipay_dict(value)
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def fail_reason_code(self):
        return self._fail_reason_code

    @fail_reason_code.setter
    def fail_reason_code(self, value):
        self._fail_reason_code = value
    @property
    def fail_reason_message(self):
        return self._fail_reason_message

    @fail_reason_message.setter
    def fail_reason_message(self, value):
        self._fail_reason_message = value
    @property
    def repayment_method_and_term_map(self):
        return self._repayment_method_and_term_map

    @repayment_method_and_term_map.setter
    def repayment_method_and_term_map(self, value):
        self._repayment_method_and_term_map = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value
    @property
    def un_limit_url(self):
        return self._un_limit_url

    @un_limit_url.setter
    def un_limit_url(self, value):
        self._un_limit_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanlendElementConsultResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'default_bank_card' in response:
            self.default_bank_card = response['default_bank_card']
        if 'extension' in response:
            self.extension = response['extension']
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'fail_reason_message' in response:
            self.fail_reason_message = response['fail_reason_message']
        if 'repayment_method_and_term_map' in response:
            self.repayment_method_and_term_map = response['repayment_method_and_term_map']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'un_limit_url' in response:
            self.un_limit_url = response['un_limit_url']
