#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeUnifiedsettleInstorderQueryModel(object):

    def __init__(self):
        self._amount_range_end = None
        self._amount_range_start = None
        self._date_range_end = None
        self._date_range_start = None
        self._order_id = None
        self._payer_card_no = None
        self._payer_inst_id = None
        self._product_code = None
        self._size = None
        self._status = None

    @property
    def amount_range_end(self):
        return self._amount_range_end

    @amount_range_end.setter
    def amount_range_end(self, value):
        self._amount_range_end = value
    @property
    def amount_range_start(self):
        return self._amount_range_start

    @amount_range_start.setter
    def amount_range_start(self, value):
        self._amount_range_start = value
    @property
    def date_range_end(self):
        return self._date_range_end

    @date_range_end.setter
    def date_range_end(self, value):
        self._date_range_end = value
    @property
    def date_range_start(self):
        return self._date_range_start

    @date_range_start.setter
    def date_range_start(self, value):
        self._date_range_start = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payer_card_no(self):
        return self._payer_card_no

    @payer_card_no.setter
    def payer_card_no(self, value):
        self._payer_card_no = value
    @property
    def payer_inst_id(self):
        return self._payer_inst_id

    @payer_inst_id.setter
    def payer_inst_id(self, value):
        self._payer_inst_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_range_end:
            if hasattr(self.amount_range_end, 'to_alipay_dict'):
                params['amount_range_end'] = self.amount_range_end.to_alipay_dict()
            else:
                params['amount_range_end'] = self.amount_range_end
        if self.amount_range_start:
            if hasattr(self.amount_range_start, 'to_alipay_dict'):
                params['amount_range_start'] = self.amount_range_start.to_alipay_dict()
            else:
                params['amount_range_start'] = self.amount_range_start
        if self.date_range_end:
            if hasattr(self.date_range_end, 'to_alipay_dict'):
                params['date_range_end'] = self.date_range_end.to_alipay_dict()
            else:
                params['date_range_end'] = self.date_range_end
        if self.date_range_start:
            if hasattr(self.date_range_start, 'to_alipay_dict'):
                params['date_range_start'] = self.date_range_start.to_alipay_dict()
            else:
                params['date_range_start'] = self.date_range_start
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.payer_card_no:
            if hasattr(self.payer_card_no, 'to_alipay_dict'):
                params['payer_card_no'] = self.payer_card_no.to_alipay_dict()
            else:
                params['payer_card_no'] = self.payer_card_no
        if self.payer_inst_id:
            if hasattr(self.payer_inst_id, 'to_alipay_dict'):
                params['payer_inst_id'] = self.payer_inst_id.to_alipay_dict()
            else:
                params['payer_inst_id'] = self.payer_inst_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeUnifiedsettleInstorderQueryModel()
        if 'amount_range_end' in d:
            o.amount_range_end = d['amount_range_end']
        if 'amount_range_start' in d:
            o.amount_range_start = d['amount_range_start']
        if 'date_range_end' in d:
            o.date_range_end = d['date_range_end']
        if 'date_range_start' in d:
            o.date_range_start = d['date_range_start']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payer_card_no' in d:
            o.payer_card_no = d['payer_card_no']
        if 'payer_inst_id' in d:
            o.payer_inst_id = d['payer_inst_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'size' in d:
            o.size = d['size']
        if 'status' in d:
            o.status = d['status']
        return o


