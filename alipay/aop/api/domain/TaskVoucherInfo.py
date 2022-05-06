#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskVoucherInfo(object):

    def __init__(self):
        self._shop_voucher_sales_amount = None
        self._voucher_denomination = None
        self._voucher_icon_url = None
        self._voucher_name = None
        self._voucher_sales_amount = None
        self._voucher_template_id = None
        self._voucher_usage_threshold = None

    @property
    def shop_voucher_sales_amount(self):
        return self._shop_voucher_sales_amount

    @shop_voucher_sales_amount.setter
    def shop_voucher_sales_amount(self, value):
        self._shop_voucher_sales_amount = value
    @property
    def voucher_denomination(self):
        return self._voucher_denomination

    @voucher_denomination.setter
    def voucher_denomination(self, value):
        self._voucher_denomination = value
    @property
    def voucher_icon_url(self):
        return self._voucher_icon_url

    @voucher_icon_url.setter
    def voucher_icon_url(self, value):
        self._voucher_icon_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_sales_amount(self):
        return self._voucher_sales_amount

    @voucher_sales_amount.setter
    def voucher_sales_amount(self, value):
        self._voucher_sales_amount = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value
    @property
    def voucher_usage_threshold(self):
        return self._voucher_usage_threshold

    @voucher_usage_threshold.setter
    def voucher_usage_threshold(self, value):
        self._voucher_usage_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_voucher_sales_amount:
            if hasattr(self.shop_voucher_sales_amount, 'to_alipay_dict'):
                params['shop_voucher_sales_amount'] = self.shop_voucher_sales_amount.to_alipay_dict()
            else:
                params['shop_voucher_sales_amount'] = self.shop_voucher_sales_amount
        if self.voucher_denomination:
            if hasattr(self.voucher_denomination, 'to_alipay_dict'):
                params['voucher_denomination'] = self.voucher_denomination.to_alipay_dict()
            else:
                params['voucher_denomination'] = self.voucher_denomination
        if self.voucher_icon_url:
            if hasattr(self.voucher_icon_url, 'to_alipay_dict'):
                params['voucher_icon_url'] = self.voucher_icon_url.to_alipay_dict()
            else:
                params['voucher_icon_url'] = self.voucher_icon_url
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_sales_amount:
            if hasattr(self.voucher_sales_amount, 'to_alipay_dict'):
                params['voucher_sales_amount'] = self.voucher_sales_amount.to_alipay_dict()
            else:
                params['voucher_sales_amount'] = self.voucher_sales_amount
        if self.voucher_template_id:
            if hasattr(self.voucher_template_id, 'to_alipay_dict'):
                params['voucher_template_id'] = self.voucher_template_id.to_alipay_dict()
            else:
                params['voucher_template_id'] = self.voucher_template_id
        if self.voucher_usage_threshold:
            if hasattr(self.voucher_usage_threshold, 'to_alipay_dict'):
                params['voucher_usage_threshold'] = self.voucher_usage_threshold.to_alipay_dict()
            else:
                params['voucher_usage_threshold'] = self.voucher_usage_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskVoucherInfo()
        if 'shop_voucher_sales_amount' in d:
            o.shop_voucher_sales_amount = d['shop_voucher_sales_amount']
        if 'voucher_denomination' in d:
            o.voucher_denomination = d['voucher_denomination']
        if 'voucher_icon_url' in d:
            o.voucher_icon_url = d['voucher_icon_url']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_sales_amount' in d:
            o.voucher_sales_amount = d['voucher_sales_amount']
        if 'voucher_template_id' in d:
            o.voucher_template_id = d['voucher_template_id']
        if 'voucher_usage_threshold' in d:
            o.voucher_usage_threshold = d['voucher_usage_threshold']
        return o


