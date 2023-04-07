#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizfundSettleInfo import BizfundSettleInfo


class VoucherSaleModeInfo(object):

    def __init__(self):
        self._fund_custody_mode = None
        self._overdue_refundable = None
        self._overdue_refundable_need_confirm = None
        self._payee_pid = None
        self._refundable = None
        self._refundable_need_confirm = None
        self._sale_amount = None
        self._settle_info = None

    @property
    def fund_custody_mode(self):
        return self._fund_custody_mode

    @fund_custody_mode.setter
    def fund_custody_mode(self, value):
        self._fund_custody_mode = value
    @property
    def overdue_refundable(self):
        return self._overdue_refundable

    @overdue_refundable.setter
    def overdue_refundable(self, value):
        self._overdue_refundable = value
    @property
    def overdue_refundable_need_confirm(self):
        return self._overdue_refundable_need_confirm

    @overdue_refundable_need_confirm.setter
    def overdue_refundable_need_confirm(self, value):
        self._overdue_refundable_need_confirm = value
    @property
    def payee_pid(self):
        return self._payee_pid

    @payee_pid.setter
    def payee_pid(self, value):
        self._payee_pid = value
    @property
    def refundable(self):
        return self._refundable

    @refundable.setter
    def refundable(self, value):
        self._refundable = value
    @property
    def refundable_need_confirm(self):
        return self._refundable_need_confirm

    @refundable_need_confirm.setter
    def refundable_need_confirm(self, value):
        self._refundable_need_confirm = value
    @property
    def sale_amount(self):
        return self._sale_amount

    @sale_amount.setter
    def sale_amount(self, value):
        self._sale_amount = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, BizfundSettleInfo):
            self._settle_info = value
        else:
            self._settle_info = BizfundSettleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fund_custody_mode:
            if hasattr(self.fund_custody_mode, 'to_alipay_dict'):
                params['fund_custody_mode'] = self.fund_custody_mode.to_alipay_dict()
            else:
                params['fund_custody_mode'] = self.fund_custody_mode
        if self.overdue_refundable:
            if hasattr(self.overdue_refundable, 'to_alipay_dict'):
                params['overdue_refundable'] = self.overdue_refundable.to_alipay_dict()
            else:
                params['overdue_refundable'] = self.overdue_refundable
        if self.overdue_refundable_need_confirm:
            if hasattr(self.overdue_refundable_need_confirm, 'to_alipay_dict'):
                params['overdue_refundable_need_confirm'] = self.overdue_refundable_need_confirm.to_alipay_dict()
            else:
                params['overdue_refundable_need_confirm'] = self.overdue_refundable_need_confirm
        if self.payee_pid:
            if hasattr(self.payee_pid, 'to_alipay_dict'):
                params['payee_pid'] = self.payee_pid.to_alipay_dict()
            else:
                params['payee_pid'] = self.payee_pid
        if self.refundable:
            if hasattr(self.refundable, 'to_alipay_dict'):
                params['refundable'] = self.refundable.to_alipay_dict()
            else:
                params['refundable'] = self.refundable
        if self.refundable_need_confirm:
            if hasattr(self.refundable_need_confirm, 'to_alipay_dict'):
                params['refundable_need_confirm'] = self.refundable_need_confirm.to_alipay_dict()
            else:
                params['refundable_need_confirm'] = self.refundable_need_confirm
        if self.sale_amount:
            if hasattr(self.sale_amount, 'to_alipay_dict'):
                params['sale_amount'] = self.sale_amount.to_alipay_dict()
            else:
                params['sale_amount'] = self.sale_amount
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSaleModeInfo()
        if 'fund_custody_mode' in d:
            o.fund_custody_mode = d['fund_custody_mode']
        if 'overdue_refundable' in d:
            o.overdue_refundable = d['overdue_refundable']
        if 'overdue_refundable_need_confirm' in d:
            o.overdue_refundable_need_confirm = d['overdue_refundable_need_confirm']
        if 'payee_pid' in d:
            o.payee_pid = d['payee_pid']
        if 'refundable' in d:
            o.refundable = d['refundable']
        if 'refundable_need_confirm' in d:
            o.refundable_need_confirm = d['refundable_need_confirm']
        if 'sale_amount' in d:
            o.sale_amount = d['sale_amount']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        return o


