#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailVoucherCodeDetail import FailVoucherCodeDetail


class AlipayMarketingActivityOrdervoucherCodedepositResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherCodedepositResponse, self).__init__()
        self._fail_count = None
        self._fail_voucher_code_detail_list = None
        self._success_count = None
        self._success_voucher_code_list = None

    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def fail_voucher_code_detail_list(self):
        return self._fail_voucher_code_detail_list

    @fail_voucher_code_detail_list.setter
    def fail_voucher_code_detail_list(self, value):
        if isinstance(value, list):
            self._fail_voucher_code_detail_list = list()
            for i in value:
                if isinstance(i, FailVoucherCodeDetail):
                    self._fail_voucher_code_detail_list.append(i)
                else:
                    self._fail_voucher_code_detail_list.append(FailVoucherCodeDetail.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def success_voucher_code_list(self):
        return self._success_voucher_code_list

    @success_voucher_code_list.setter
    def success_voucher_code_list(self, value):
        if isinstance(value, list):
            self._success_voucher_code_list = list()
            for i in value:
                self._success_voucher_code_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherCodedepositResponse, self).parse_response_content(response_content)
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'fail_voucher_code_detail_list' in response:
            self.fail_voucher_code_detail_list = response['fail_voucher_code_detail_list']
        if 'success_count' in response:
            self.success_count = response['success_count']
        if 'success_voucher_code_list' in response:
            self.success_voucher_code_list = response['success_voucher_code_list']
