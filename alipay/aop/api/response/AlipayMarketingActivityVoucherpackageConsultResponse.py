#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherPackageConsultResult import VoucherPackageConsultResult


class AlipayMarketingActivityVoucherpackageConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherpackageConsultResponse, self).__init__()
        self._voucher_package_consult_result = None

    @property
    def voucher_package_consult_result(self):
        return self._voucher_package_consult_result

    @voucher_package_consult_result.setter
    def voucher_package_consult_result(self, value):
        if isinstance(value, list):
            self._voucher_package_consult_result = list()
            for i in value:
                if isinstance(i, VoucherPackageConsultResult):
                    self._voucher_package_consult_result.append(i)
                else:
                    self._voucher_package_consult_result.append(VoucherPackageConsultResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherpackageConsultResponse, self).parse_response_content(response_content)
        if 'voucher_package_consult_result' in response:
            self.voucher_package_consult_result = response['voucher_package_consult_result']
