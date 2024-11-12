#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardDeductionorderBatchqueryModel(object):

    def __init__(self):
        self._card_id = None
        self._card_type = None
        self._deduction_end_date = None
        self._deduction_order_type = None
        self._deduction_start_date = None
        self._deduction_status = None
        self._open_id = None
        self._order_end_date = None
        self._order_start_date = None
        self._page_num = None
        self._page_size = None
        self._shop_id = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def deduction_end_date(self):
        return self._deduction_end_date

    @deduction_end_date.setter
    def deduction_end_date(self, value):
        self._deduction_end_date = value
    @property
    def deduction_order_type(self):
        return self._deduction_order_type

    @deduction_order_type.setter
    def deduction_order_type(self, value):
        self._deduction_order_type = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.deduction_end_date:
            if hasattr(self.deduction_end_date, 'to_alipay_dict'):
                params['deduction_end_date'] = self.deduction_end_date.to_alipay_dict()
            else:
                params['deduction_end_date'] = self.deduction_end_date
        if self.deduction_order_type:
            if hasattr(self.deduction_order_type, 'to_alipay_dict'):
                params['deduction_order_type'] = self.deduction_order_type.to_alipay_dict()
            else:
                params['deduction_order_type'] = self.deduction_order_type
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardDeductionorderBatchqueryModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'deduction_end_date' in d:
            o.deduction_end_date = d['deduction_end_date']
        if 'deduction_order_type' in d:
            o.deduction_order_type = d['deduction_order_type']
        if 'deduction_start_date' in d:
            o.deduction_start_date = d['deduction_start_date']
        if 'deduction_status' in d:
            o.deduction_status = d['deduction_status']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_end_date' in d:
            o.order_end_date = d['order_end_date']
        if 'order_start_date' in d:
            o.order_start_date = d['order_start_date']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


