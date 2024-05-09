#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardDeductionorderBatchqueryModel(object):

    def __init__(self):
        self._card_id = None
        self._deduction_end_date = None
        self._deduction_start_date = None
        self._deduction_status = None
        self._order_end_date = None
        self._order_start_date = None
        self._page_num = None
        self._page_size = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def deduction_end_date(self):
        return self._deduction_end_date

    @deduction_end_date.setter
    def deduction_end_date(self, value):
        self._deduction_end_date = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.deduction_end_date:
            if hasattr(self.deduction_end_date, 'to_alipay_dict'):
                params['deduction_end_date'] = self.deduction_end_date.to_alipay_dict()
            else:
                params['deduction_end_date'] = self.deduction_end_date
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardDeductionorderBatchqueryModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'deduction_end_date' in d:
            o.deduction_end_date = d['deduction_end_date']
        if 'deduction_start_date' in d:
            o.deduction_start_date = d['deduction_start_date']
        if 'deduction_status' in d:
            o.deduction_status = d['deduction_status']
        if 'order_end_date' in d:
            o.order_end_date = d['order_end_date']
        if 'order_start_date' in d:
            o.order_start_date = d['order_start_date']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


