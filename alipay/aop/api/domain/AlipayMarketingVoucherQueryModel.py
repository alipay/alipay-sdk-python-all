#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherQueryModel(object):

    def __init__(self):
        self._voucher_id = None

    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayMarketingVoucherQueryModel()
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


