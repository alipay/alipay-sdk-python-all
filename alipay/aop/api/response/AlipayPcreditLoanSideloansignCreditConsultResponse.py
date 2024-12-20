#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstitutionVO import InstitutionVO


class AlipayPcreditLoanSideloansignCreditConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloansignCreditConsultResponse, self).__init__()
        self._admit = None
        self._alipay_desensitize_login_id = None
        self._extension = None
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._fund_supplier = None
        self._other_alipay_densey_login_id = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._un_limit_url = None
        self._user_desensitize_name = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def alipay_desensitize_login_id(self):
        return self._alipay_desensitize_login_id

    @alipay_desensitize_login_id.setter
    def alipay_desensitize_login_id(self, value):
        self._alipay_desensitize_login_id = value
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
    def fund_supplier(self):
        return self._fund_supplier

    @fund_supplier.setter
    def fund_supplier(self, value):
        if isinstance(value, InstitutionVO):
            self._fund_supplier = value
        else:
            self._fund_supplier = InstitutionVO.from_alipay_dict(value)
    @property
    def other_alipay_densey_login_id(self):
        return self._other_alipay_densey_login_id

    @other_alipay_densey_login_id.setter
    def other_alipay_densey_login_id(self, value):
        self._other_alipay_densey_login_id = value
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
    @property
    def user_desensitize_name(self):
        return self._user_desensitize_name

    @user_desensitize_name.setter
    def user_desensitize_name(self, value):
        self._user_desensitize_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloansignCreditConsultResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'alipay_desensitize_login_id' in response:
            self.alipay_desensitize_login_id = response['alipay_desensitize_login_id']
        if 'extension' in response:
            self.extension = response['extension']
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'fail_reason_message' in response:
            self.fail_reason_message = response['fail_reason_message']
        if 'fund_supplier' in response:
            self.fund_supplier = response['fund_supplier']
        if 'other_alipay_densey_login_id' in response:
            self.other_alipay_densey_login_id = response['other_alipay_densey_login_id']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'un_limit_url' in response:
            self.un_limit_url = response['un_limit_url']
        if 'user_desensitize_name' in response:
            self.user_desensitize_name = response['user_desensitize_name']
