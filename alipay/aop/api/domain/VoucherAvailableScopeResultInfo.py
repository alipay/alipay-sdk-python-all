#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableGeographyScopeResultInfo import VoucherAvailableGeographyScopeResultInfo


class VoucherAvailableScopeResultInfo(object):

    def __init__(self):
        self._voucher_available_geography_scope_result_info = None

    @property
    def voucher_available_geography_scope_result_info(self):
        return self._voucher_available_geography_scope_result_info

    @voucher_available_geography_scope_result_info.setter
    def voucher_available_geography_scope_result_info(self, value):
        if isinstance(value, VoucherAvailableGeographyScopeResultInfo):
            self._voucher_available_geography_scope_result_info = value
        else:
            self._voucher_available_geography_scope_result_info = VoucherAvailableGeographyScopeResultInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_available_geography_scope_result_info:
            if hasattr(self.voucher_available_geography_scope_result_info, 'to_alipay_dict'):
                params['voucher_available_geography_scope_result_info'] = self.voucher_available_geography_scope_result_info.to_alipay_dict()
            else:
                params['voucher_available_geography_scope_result_info'] = self.voucher_available_geography_scope_result_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableScopeResultInfo()
        if 'voucher_available_geography_scope_result_info' in d:
            o.voucher_available_geography_scope_result_info = d['voucher_available_geography_scope_result_info']
        return o


