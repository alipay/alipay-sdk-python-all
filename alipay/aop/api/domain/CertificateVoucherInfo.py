#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateVoucherInfo(object):

    def __init__(self):
        self._voucher_code = None
        self._voucher_id = None

    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_code:
            if hasattr(self.voucher_code, 'to_alipay_dict'):
                params['voucher_code'] = self.voucher_code.to_alipay_dict()
            else:
                params['voucher_code'] = self.voucher_code
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateVoucherInfo()
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


