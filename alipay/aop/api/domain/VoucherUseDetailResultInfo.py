#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherUseDetailResultInfo(object):

    def __init__(self):
        self._voucher_max_un_use_times = None

    @property
    def voucher_max_un_use_times(self):
        return self._voucher_max_un_use_times

    @voucher_max_un_use_times.setter
    def voucher_max_un_use_times(self, value):
        self._voucher_max_un_use_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_max_un_use_times:
            if hasattr(self.voucher_max_un_use_times, 'to_alipay_dict'):
                params['voucher_max_un_use_times'] = self.voucher_max_un_use_times.to_alipay_dict()
            else:
                params['voucher_max_un_use_times'] = self.voucher_max_un_use_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseDetailResultInfo()
        if 'voucher_max_un_use_times' in d:
            o.voucher_max_un_use_times = d['voucher_max_un_use_times']
        return o


