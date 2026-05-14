#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AplusOrderDetailList(object):

    def __init__(self):
        self._certificate_count = None
        self._certificate_id_list = None
        self._certificate_status_mapping = None
        self._gmt_create = None
        self._gmt_modified = None
        self._item_id = None
        self._item_title = None
        self._merchant_discount = None
        self._merchant_real_receipt_amount = None
        self._order_id = None
        self._order_status = None
        self._partner_id = None
        self._partner_open_id = None
        self._platform_discount = None
        self._real_pay_amount = None
        self._third_discount = None
        self._total_amount = None
        self._trade_no = None
        self._user_id = None
        self._user_open_id = None

    @property
    def certificate_count(self):
        return self._certificate_count

    @certificate_count.setter
    def certificate_count(self, value):
        self._certificate_count = value
    @property
    def certificate_id_list(self):
        return self._certificate_id_list

    @certificate_id_list.setter
    def certificate_id_list(self, value):
        self._certificate_id_list = value
    @property
    def certificate_status_mapping(self):
        return self._certificate_status_mapping

    @certificate_status_mapping.setter
    def certificate_status_mapping(self, value):
        self._certificate_status_mapping = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def merchant_discount(self):
        return self._merchant_discount

    @merchant_discount.setter
    def merchant_discount(self, value):
        self._merchant_discount = value
    @property
    def merchant_real_receipt_amount(self):
        return self._merchant_real_receipt_amount

    @merchant_real_receipt_amount.setter
    def merchant_real_receipt_amount(self, value):
        self._merchant_real_receipt_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_open_id(self):
        return self._partner_open_id

    @partner_open_id.setter
    def partner_open_id(self, value):
        self._partner_open_id = value
    @property
    def platform_discount(self):
        return self._platform_discount

    @platform_discount.setter
    def platform_discount(self, value):
        self._platform_discount = value
    @property
    def real_pay_amount(self):
        return self._real_pay_amount

    @real_pay_amount.setter
    def real_pay_amount(self, value):
        self._real_pay_amount = value
    @property
    def third_discount(self):
        return self._third_discount

    @third_discount.setter
    def third_discount(self, value):
        self._third_discount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_count:
            if hasattr(self.certificate_count, 'to_alipay_dict'):
                params['certificate_count'] = self.certificate_count.to_alipay_dict()
            else:
                params['certificate_count'] = self.certificate_count
        if self.certificate_id_list:
            if hasattr(self.certificate_id_list, 'to_alipay_dict'):
                params['certificate_id_list'] = self.certificate_id_list.to_alipay_dict()
            else:
                params['certificate_id_list'] = self.certificate_id_list
        if self.certificate_status_mapping:
            if hasattr(self.certificate_status_mapping, 'to_alipay_dict'):
                params['certificate_status_mapping'] = self.certificate_status_mapping.to_alipay_dict()
            else:
                params['certificate_status_mapping'] = self.certificate_status_mapping
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.merchant_discount:
            if hasattr(self.merchant_discount, 'to_alipay_dict'):
                params['merchant_discount'] = self.merchant_discount.to_alipay_dict()
            else:
                params['merchant_discount'] = self.merchant_discount
        if self.merchant_real_receipt_amount:
            if hasattr(self.merchant_real_receipt_amount, 'to_alipay_dict'):
                params['merchant_real_receipt_amount'] = self.merchant_real_receipt_amount.to_alipay_dict()
            else:
                params['merchant_real_receipt_amount'] = self.merchant_real_receipt_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_open_id:
            if hasattr(self.partner_open_id, 'to_alipay_dict'):
                params['partner_open_id'] = self.partner_open_id.to_alipay_dict()
            else:
                params['partner_open_id'] = self.partner_open_id
        if self.platform_discount:
            if hasattr(self.platform_discount, 'to_alipay_dict'):
                params['platform_discount'] = self.platform_discount.to_alipay_dict()
            else:
                params['platform_discount'] = self.platform_discount
        if self.real_pay_amount:
            if hasattr(self.real_pay_amount, 'to_alipay_dict'):
                params['real_pay_amount'] = self.real_pay_amount.to_alipay_dict()
            else:
                params['real_pay_amount'] = self.real_pay_amount
        if self.third_discount:
            if hasattr(self.third_discount, 'to_alipay_dict'):
                params['third_discount'] = self.third_discount.to_alipay_dict()
            else:
                params['third_discount'] = self.third_discount
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AplusOrderDetailList()
        if 'certificate_count' in d:
            o.certificate_count = d['certificate_count']
        if 'certificate_id_list' in d:
            o.certificate_id_list = d['certificate_id_list']
        if 'certificate_status_mapping' in d:
            o.certificate_status_mapping = d['certificate_status_mapping']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'merchant_discount' in d:
            o.merchant_discount = d['merchant_discount']
        if 'merchant_real_receipt_amount' in d:
            o.merchant_real_receipt_amount = d['merchant_real_receipt_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_open_id' in d:
            o.partner_open_id = d['partner_open_id']
        if 'platform_discount' in d:
            o.platform_discount = d['platform_discount']
        if 'real_pay_amount' in d:
            o.real_pay_amount = d['real_pay_amount']
        if 'third_discount' in d:
            o.third_discount = d['third_discount']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o


