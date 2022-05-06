#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskVoucherBasicInfo(object):

    def __init__(self):
        self._logo = None
        self._reduction_amount = None
        self._threshold_amount = None
        self._total_used_count = None
        self._used_count = None
        self._voucher_name = None
        self._voucher_template_no = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def total_used_count(self):
        return self._total_used_count

    @total_used_count.setter
    def total_used_count(self, value):
        self._total_used_count = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_template_no(self):
        return self._voucher_template_no

    @voucher_template_no.setter
    def voucher_template_no(self, value):
        self._voucher_template_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.total_used_count:
            if hasattr(self.total_used_count, 'to_alipay_dict'):
                params['total_used_count'] = self.total_used_count.to_alipay_dict()
            else:
                params['total_used_count'] = self.total_used_count
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_template_no:
            if hasattr(self.voucher_template_no, 'to_alipay_dict'):
                params['voucher_template_no'] = self.voucher_template_no.to_alipay_dict()
            else:
                params['voucher_template_no'] = self.voucher_template_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskVoucherBasicInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'total_used_count' in d:
            o.total_used_count = d['total_used_count']
        if 'used_count' in d:
            o.used_count = d['used_count']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_template_no' in d:
            o.voucher_template_no = d['voucher_template_no']
        return o


