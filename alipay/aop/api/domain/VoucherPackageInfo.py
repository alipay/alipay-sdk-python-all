#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherPackageBaseInfo import VoucherPackageBaseInfo
from alipay.aop.api.domain.VoucherPackageSalesLiteInfo import VoucherPackageSalesLiteInfo


class VoucherPackageInfo(object):

    def __init__(self):
        self._voucher_package_base_info = None
        self._voucher_package_sales_lite_info = None

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
    def voucher_package_sales_lite_info(self):
        return self._voucher_package_sales_lite_info

    @voucher_package_sales_lite_info.setter
    def voucher_package_sales_lite_info(self, value):
        if isinstance(value, VoucherPackageSalesLiteInfo):
            self._voucher_package_sales_lite_info = value
        else:
            self._voucher_package_sales_lite_info = VoucherPackageSalesLiteInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_package_base_info:
            if hasattr(self.voucher_package_base_info, 'to_alipay_dict'):
                params['voucher_package_base_info'] = self.voucher_package_base_info.to_alipay_dict()
            else:
                params['voucher_package_base_info'] = self.voucher_package_base_info
        if self.voucher_package_sales_lite_info:
            if hasattr(self.voucher_package_sales_lite_info, 'to_alipay_dict'):
                params['voucher_package_sales_lite_info'] = self.voucher_package_sales_lite_info.to_alipay_dict()
            else:
                params['voucher_package_sales_lite_info'] = self.voucher_package_sales_lite_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageInfo()
        if 'voucher_package_base_info' in d:
            o.voucher_package_base_info = d['voucher_package_base_info']
        if 'voucher_package_sales_lite_info' in d:
            o.voucher_package_sales_lite_info = d['voucher_package_sales_lite_info']
        return o


