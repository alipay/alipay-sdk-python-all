#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityVoucherpackageBatchqueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._voucher_package_purchase_start_time = None
        self._voucher_package_status = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def voucher_package_purchase_start_time(self):
        return self._voucher_package_purchase_start_time

    @voucher_package_purchase_start_time.setter
    def voucher_package_purchase_start_time(self, value):
        self._voucher_package_purchase_start_time = value
    @property
    def voucher_package_status(self):
        return self._voucher_package_status

    @voucher_package_status.setter
    def voucher_package_status(self, value):
        self._voucher_package_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.voucher_package_purchase_start_time:
            if hasattr(self.voucher_package_purchase_start_time, 'to_alipay_dict'):
                params['voucher_package_purchase_start_time'] = self.voucher_package_purchase_start_time.to_alipay_dict()
            else:
                params['voucher_package_purchase_start_time'] = self.voucher_package_purchase_start_time
        if self.voucher_package_status:
            if hasattr(self.voucher_package_status, 'to_alipay_dict'):
                params['voucher_package_status'] = self.voucher_package_status.to_alipay_dict()
            else:
                params['voucher_package_status'] = self.voucher_package_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityVoucherpackageBatchqueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'voucher_package_purchase_start_time' in d:
            o.voucher_package_purchase_start_time = d['voucher_package_purchase_start_time']
        if 'voucher_package_status' in d:
            o.voucher_package_status = d['voucher_package_status']
        return o


