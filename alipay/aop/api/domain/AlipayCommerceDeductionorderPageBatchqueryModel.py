#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDeductionorderPageBatchqueryModel(object):

    def __init__(self):
        self._card_id = None
        self._card_name = None
        self._deduction_end_date = None
        self._deduction_order_id = None
        self._deduction_start_date = None
        self._deduction_status = None
        self._merchant_pid = None
        self._order_end_date = None
        self._order_start_date = None
        self._page_num = None
        self._page_size = None
        self._settle_status = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def deduction_end_date(self):
        return self._deduction_end_date

    @deduction_end_date.setter
    def deduction_end_date(self, value):
        self._deduction_end_date = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def deduction_start_date(self):
        return self._deduction_start_date

    @deduction_start_date.setter
    def deduction_start_date(self, value):
        self._deduction_start_date = value
    @property
    def deduction_status(self):
        return self._deduction_status

    @deduction_status.setter
    def deduction_status(self, value):
        self._deduction_status = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_end_date(self):
        return self._order_end_date

    @order_end_date.setter
    def order_end_date(self, value):
        self._order_end_date = value
    @property
    def order_start_date(self):
        return self._order_start_date

    @order_start_date.setter
    def order_start_date(self, value):
        self._order_start_date = value
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
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.deduction_end_date:
            if hasattr(self.deduction_end_date, 'to_alipay_dict'):
                params['deduction_end_date'] = self.deduction_end_date.to_alipay_dict()
            else:
                params['deduction_end_date'] = self.deduction_end_date
        if self.deduction_order_id:
            if hasattr(self.deduction_order_id, 'to_alipay_dict'):
                params['deduction_order_id'] = self.deduction_order_id.to_alipay_dict()
            else:
                params['deduction_order_id'] = self.deduction_order_id
        if self.deduction_start_date:
            if hasattr(self.deduction_start_date, 'to_alipay_dict'):
                params['deduction_start_date'] = self.deduction_start_date.to_alipay_dict()
            else:
                params['deduction_start_date'] = self.deduction_start_date
        if self.deduction_status:
            if hasattr(self.deduction_status, 'to_alipay_dict'):
                params['deduction_status'] = self.deduction_status.to_alipay_dict()
            else:
                params['deduction_status'] = self.deduction_status
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.order_end_date:
            if hasattr(self.order_end_date, 'to_alipay_dict'):
                params['order_end_date'] = self.order_end_date.to_alipay_dict()
            else:
                params['order_end_date'] = self.order_end_date
        if self.order_start_date:
            if hasattr(self.order_start_date, 'to_alipay_dict'):
                params['order_start_date'] = self.order_start_date.to_alipay_dict()
            else:
                params['order_start_date'] = self.order_start_date
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
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDeductionorderPageBatchqueryModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'deduction_end_date' in d:
            o.deduction_end_date = d['deduction_end_date']
        if 'deduction_order_id' in d:
            o.deduction_order_id = d['deduction_order_id']
        if 'deduction_start_date' in d:
            o.deduction_start_date = d['deduction_start_date']
        if 'deduction_status' in d:
            o.deduction_status = d['deduction_status']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'order_end_date' in d:
            o.order_end_date = d['order_end_date']
        if 'order_start_date' in d:
            o.order_start_date = d['order_start_date']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        return o


