#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivitySendVoucherInfo(object):

    def __init__(self):
        self._activity_id = None
        self._merchant_order_url = None
        self._out_biz_no = None
        self._voucher_code = None
        self._voucher_code_url = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def merchant_order_url(self):
        return self._merchant_order_url

    @merchant_order_url.setter
    def merchant_order_url(self, value):
        self._merchant_order_url = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value
    @property
    def voucher_code_url(self):
        return self._voucher_code_url

    @voucher_code_url.setter
    def voucher_code_url(self, value):
        self._voucher_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.merchant_order_url:
            if hasattr(self.merchant_order_url, 'to_alipay_dict'):
                params['merchant_order_url'] = self.merchant_order_url.to_alipay_dict()
            else:
                params['merchant_order_url'] = self.merchant_order_url
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.voucher_code:
            if hasattr(self.voucher_code, 'to_alipay_dict'):
                params['voucher_code'] = self.voucher_code.to_alipay_dict()
            else:
                params['voucher_code'] = self.voucher_code
        if self.voucher_code_url:
            if hasattr(self.voucher_code_url, 'to_alipay_dict'):
                params['voucher_code_url'] = self.voucher_code_url.to_alipay_dict()
            else:
                params['voucher_code_url'] = self.voucher_code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivitySendVoucherInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'merchant_order_url' in d:
            o.merchant_order_url = d['merchant_order_url']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        if 'voucher_code_url' in d:
            o.voucher_code_url = d['voucher_code_url']
        return o


