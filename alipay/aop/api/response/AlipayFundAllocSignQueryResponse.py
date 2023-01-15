#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgreementLimitMerchant import AgreementLimitMerchant


class AlipayFundAllocSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAllocSignQueryResponse, self).__init__()
        self._agreement_no = None
        self._alloc_upper_limit = None
        self._invalid_time = None
        self._principal_id = None
        self._principal_open_id = None
        self._status = None
        self._support_merchant_list = None
        self._valid_strat_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alloc_upper_limit(self):
        return self._alloc_upper_limit

    @alloc_upper_limit.setter
    def alloc_upper_limit(self, value):
        self._alloc_upper_limit = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_open_id(self):
        return self._principal_open_id

    @principal_open_id.setter
    def principal_open_id(self, value):
        self._principal_open_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def support_merchant_list(self):
        return self._support_merchant_list

    @support_merchant_list.setter
    def support_merchant_list(self, value):
        if isinstance(value, list):
            self._support_merchant_list = list()
            for i in value:
                if isinstance(i, AgreementLimitMerchant):
                    self._support_merchant_list.append(i)
                else:
                    self._support_merchant_list.append(AgreementLimitMerchant.from_alipay_dict(i))
    @property
    def valid_strat_time(self):
        return self._valid_strat_time

    @valid_strat_time.setter
    def valid_strat_time(self, value):
        self._valid_strat_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAllocSignQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alloc_upper_limit' in response:
            self.alloc_upper_limit = response['alloc_upper_limit']
        if 'invalid_time' in response:
            self.invalid_time = response['invalid_time']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'principal_open_id' in response:
            self.principal_open_id = response['principal_open_id']
        if 'status' in response:
            self.status = response['status']
        if 'support_merchant_list' in response:
            self.support_merchant_list = response['support_merchant_list']
        if 'valid_strat_time' in response:
            self.valid_strat_time = response['valid_strat_time']
