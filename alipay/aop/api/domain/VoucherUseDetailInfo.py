#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherUseDetailInfo(object):

    def __init__(self):
        self._voucher_use_times = None

    @property
    def voucher_use_times(self):
        return self._voucher_use_times

    @voucher_use_times.setter
    def voucher_use_times(self, value):
        self._voucher_use_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_use_times:
            if hasattr(self.voucher_use_times, 'to_alipay_dict'):
                params['voucher_use_times'] = self.voucher_use_times.to_alipay_dict()
            else:
                params['voucher_use_times'] = self.voucher_use_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseDetailInfo()
        if 'voucher_use_times' in d:
            o.voucher_use_times = d['voucher_use_times']
        return o


