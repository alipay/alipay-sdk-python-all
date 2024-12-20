#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgreementView import AgreementView


class AlipayPcreditLoanSideloansignAgreementPullResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloansignAgreementPullResponse, self).__init__()
        self._agreement_list = None
        self._extension = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def agreement_list(self):
        return self._agreement_list

    @agreement_list.setter
    def agreement_list(self, value):
        if isinstance(value, list):
            self._agreement_list = list()
            for i in value:
                if isinstance(i, AgreementView):
                    self._agreement_list.append(i)
                else:
                    self._agreement_list.append(AgreementView.from_alipay_dict(i))
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloansignAgreementPullResponse, self).parse_response_content(response_content)
        if 'agreement_list' in response:
            self.agreement_list = response['agreement_list']
        if 'extension' in response:
            self.extension = response['extension']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
