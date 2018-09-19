#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BudgetInfo import BudgetInfo
from alipay.aop.api.domain.PeriodInfo import PeriodInfo
from alipay.aop.api.domain.VoucherModifyInfo import VoucherModifyInfo


class AlipayOfflineMarketingVoucherModifyModel(object):

    def __init__(self):
        self._budget_info = None
        self._ext_info = None
        self._get_count_limit = None
        self._out_biz_no = None
        self._voucher_info = None

    @property
    def budget_info(self):
        return self._budget_info

    @budget_info.setter
    def budget_info(self, value):
        if isinstance(value, BudgetInfo):
            self._budget_info = value
        else:
            self._budget_info = BudgetInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def get_count_limit(self):
        return self._get_count_limit

    @get_count_limit.setter
    def get_count_limit(self, value):
        if isinstance(value, PeriodInfo):
            self._get_count_limit = value
        else:
            self._get_count_limit = PeriodInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, VoucherModifyInfo):
            self._voucher_info = value
        else:
            self._voucher_info = VoucherModifyInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.budget_info:
            if hasattr(self.budget_info, 'to_alipay_dict'):
                params['budget_info'] = self.budget_info.to_alipay_dict()
            else:
                params['budget_info'] = self.budget_info
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.get_count_limit:
            if hasattr(self.get_count_limit, 'to_alipay_dict'):
                params['get_count_limit'] = self.get_count_limit.to_alipay_dict()
            else:
                params['get_count_limit'] = self.get_count_limit
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.voucher_info:
            if hasattr(self.voucher_info, 'to_alipay_dict'):
                params['voucher_info'] = self.voucher_info.to_alipay_dict()
            else:
                params['voucher_info'] = self.voucher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketingVoucherModifyModel()
        if 'budget_info' in d:
            o.budget_info = d['budget_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'get_count_limit' in d:
            o.get_count_limit = d['get_count_limit']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'voucher_info' in d:
            o.voucher_info = d['voucher_info']
        return o


