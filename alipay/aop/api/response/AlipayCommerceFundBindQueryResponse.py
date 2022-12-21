#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundBankCardInfoDTO import FundBankCardInfoDTO
from alipay.aop.api.domain.WithholdAgreementInfoDTO import WithholdAgreementInfoDTO


class AlipayCommerceFundBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceFundBindQueryResponse, self).__init__()
        self._bank_card_info = None
        self._bind_error_code = None
        self._bind_error_msg = None
        self._cert_no = None
        self._cert_type = None
        self._open_id = None
        self._out_bind_no = None
        self._real_name = None
        self._status = None
        self._user_id = None
        self._withhold_agreement_info = None

    @property
    def bank_card_info(self):
        return self._bank_card_info

    @bank_card_info.setter
    def bank_card_info(self, value):
        if isinstance(value, FundBankCardInfoDTO):
            self._bank_card_info = value
        else:
            self._bank_card_info = FundBankCardInfoDTO.from_alipay_dict(value)
    @property
    def bind_error_code(self):
        return self._bind_error_code

    @bind_error_code.setter
    def bind_error_code(self, value):
        self._bind_error_code = value
    @property
    def bind_error_msg(self):
        return self._bind_error_msg

    @bind_error_msg.setter
    def bind_error_msg(self, value):
        self._bind_error_msg = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_bind_no(self):
        return self._out_bind_no

    @out_bind_no.setter
    def out_bind_no(self, value):
        self._out_bind_no = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def withhold_agreement_info(self):
        return self._withhold_agreement_info

    @withhold_agreement_info.setter
    def withhold_agreement_info(self, value):
        if isinstance(value, WithholdAgreementInfoDTO):
            self._withhold_agreement_info = value
        else:
            self._withhold_agreement_info = WithholdAgreementInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceFundBindQueryResponse, self).parse_response_content(response_content)
        if 'bank_card_info' in response:
            self.bank_card_info = response['bank_card_info']
        if 'bind_error_code' in response:
            self.bind_error_code = response['bind_error_code']
        if 'bind_error_msg' in response:
            self.bind_error_msg = response['bind_error_msg']
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_bind_no' in response:
            self.out_bind_no = response['out_bind_no']
        if 'real_name' in response:
            self.real_name = response['real_name']
        if 'status' in response:
            self.status = response['status']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'withhold_agreement_info' in response:
            self.withhold_agreement_info = response['withhold_agreement_info']
