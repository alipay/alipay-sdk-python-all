#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherPackageConsultResult(object):

    def __init__(self):
        self._consult_result_code = None
        self._voucher_package_id = None

    @property
    def consult_result_code(self):
        return self._consult_result_code

    @consult_result_code.setter
    def consult_result_code(self, value):
        self._consult_result_code = value
    @property
    def voucher_package_id(self):
        return self._voucher_package_id

    @voucher_package_id.setter
    def voucher_package_id(self, value):
        self._voucher_package_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_result_code:
            if hasattr(self.consult_result_code, 'to_alipay_dict'):
                params['consult_result_code'] = self.consult_result_code.to_alipay_dict()
            else:
                params['consult_result_code'] = self.consult_result_code
        if self.voucher_package_id:
            if hasattr(self.voucher_package_id, 'to_alipay_dict'):
                params['voucher_package_id'] = self.voucher_package_id.to_alipay_dict()
            else:
                params['voucher_package_id'] = self.voucher_package_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageConsultResult()
        if 'consult_result_code' in d:
            o.consult_result_code = d['consult_result_code']
        if 'voucher_package_id' in d:
            o.voucher_package_id = d['voucher_package_id']
        return o


