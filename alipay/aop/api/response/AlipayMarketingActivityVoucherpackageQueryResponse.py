#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherPackageActivityInfo import VoucherPackageActivityInfo
from alipay.aop.api.domain.VoucherPackageBaseInfo import VoucherPackageBaseInfo
from alipay.aop.api.domain.VoucherPackageSalesInfo import VoucherPackageSalesInfo
from alipay.aop.api.domain.VoucherPackageUseRule import VoucherPackageUseRule


class AlipayMarketingActivityVoucherpackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherpackageQueryResponse, self).__init__()
        self._voucher_package_activity_info = None
        self._voucher_package_base_info = None
        self._voucher_package_sales_info = None
        self._voucher_package_use_rule = None

    @property
    def voucher_package_activity_info(self):
        return self._voucher_package_activity_info

    @voucher_package_activity_info.setter
    def voucher_package_activity_info(self, value):
        if isinstance(value, list):
            self._voucher_package_activity_info = list()
            for i in value:
                if isinstance(i, VoucherPackageActivityInfo):
                    self._voucher_package_activity_info.append(i)
                else:
                    self._voucher_package_activity_info.append(VoucherPackageActivityInfo.from_alipay_dict(i))
    @property
    def voucher_package_base_info(self):
        return self._voucher_package_base_info

    @voucher_package_base_info.setter
    def voucher_package_base_info(self, value):
        if isinstance(value, VoucherPackageBaseInfo):
            self._voucher_package_base_info = value
        else:
            self._voucher_package_base_info = VoucherPackageBaseInfo.from_alipay_dict(value)
    @property
    def voucher_package_sales_info(self):
        return self._voucher_package_sales_info

    @voucher_package_sales_info.setter
    def voucher_package_sales_info(self, value):
        if isinstance(value, VoucherPackageSalesInfo):
            self._voucher_package_sales_info = value
        else:
            self._voucher_package_sales_info = VoucherPackageSalesInfo.from_alipay_dict(value)
    @property
    def voucher_package_use_rule(self):
        return self._voucher_package_use_rule

    @voucher_package_use_rule.setter
    def voucher_package_use_rule(self, value):
        if isinstance(value, VoucherPackageUseRule):
            self._voucher_package_use_rule = value
        else:
            self._voucher_package_use_rule = VoucherPackageUseRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherpackageQueryResponse, self).parse_response_content(response_content)
        if 'voucher_package_activity_info' in response:
            self.voucher_package_activity_info = response['voucher_package_activity_info']
        if 'voucher_package_base_info' in response:
            self.voucher_package_base_info = response['voucher_package_base_info']
        if 'voucher_package_sales_info' in response:
            self.voucher_package_sales_info = response['voucher_package_sales_info']
        if 'voucher_package_use_rule' in response:
            self.voucher_package_use_rule = response['voucher_package_use_rule']
