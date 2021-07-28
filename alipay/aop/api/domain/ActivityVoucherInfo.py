#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherItem import VoucherItem


class ActivityVoucherInfo(object):

    def __init__(self):
        self._activity_id = None
        self._activity_name = None
        self._activity_status = None
        self._merchant_logo = None
        self._merchant_name = None
        self._voucher_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, VoucherItem):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(VoucherItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.voucher_list:
            if isinstance(self.voucher_list, list):
                for i in range(0, len(self.voucher_list)):
                    element = self.voucher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_list, 'to_alipay_dict'):
                params['voucher_list'] = self.voucher_list.to_alipay_dict()
            else:
                params['voucher_list'] = self.voucher_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityVoucherInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'voucher_list' in d:
            o.voucher_list = d['voucher_list']
        return o


