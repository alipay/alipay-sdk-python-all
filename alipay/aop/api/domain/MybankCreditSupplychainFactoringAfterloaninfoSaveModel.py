#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainFactoringAfterloaninfoSaveModel(object):

    def __init__(self):
        self._activate_state = None
        self._activate_time = None
        self._biz_order_no = None
        self._buyer_alipay_id = None
        self._equipment_name = None
        self._equipment_no = None
        self._ext_data = None
        self._invoice_number = None
        self._logistics_order_no = None
        self._order_status = None
        self._out_order_no = None
        self._preauth_freeze_time = None
        self._seller_login_id = None
        self._store_name = None
        self._store_no = None
        self._term = None
        self._total_amount = None

    @property
    def activate_state(self):
        return self._activate_state

    @activate_state.setter
    def activate_state(self, value):
        self._activate_state = value
    @property
    def activate_time(self):
        return self._activate_time

    @activate_time.setter
    def activate_time(self, value):
        self._activate_time = value
    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def buyer_alipay_id(self):
        return self._buyer_alipay_id

    @buyer_alipay_id.setter
    def buyer_alipay_id(self, value):
        self._buyer_alipay_id = value
    @property
    def equipment_name(self):
        return self._equipment_name

    @equipment_name.setter
    def equipment_name(self, value):
        self._equipment_name = value
    @property
    def equipment_no(self):
        return self._equipment_no

    @equipment_no.setter
    def equipment_no(self, value):
        self._equipment_no = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self._invoice_number = value
    @property
    def logistics_order_no(self):
        return self._logistics_order_no

    @logistics_order_no.setter
    def logistics_order_no(self, value):
        self._logistics_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def preauth_freeze_time(self):
        return self._preauth_freeze_time

    @preauth_freeze_time.setter
    def preauth_freeze_time(self, value):
        self._preauth_freeze_time = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_no(self):
        return self._store_no

    @store_no.setter
    def store_no(self, value):
        self._store_no = value
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.activate_state:
            if hasattr(self.activate_state, 'to_alipay_dict'):
                params['activate_state'] = self.activate_state.to_alipay_dict()
            else:
                params['activate_state'] = self.activate_state
        if self.activate_time:
            if hasattr(self.activate_time, 'to_alipay_dict'):
                params['activate_time'] = self.activate_time.to_alipay_dict()
            else:
                params['activate_time'] = self.activate_time
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.buyer_alipay_id:
            if hasattr(self.buyer_alipay_id, 'to_alipay_dict'):
                params['buyer_alipay_id'] = self.buyer_alipay_id.to_alipay_dict()
            else:
                params['buyer_alipay_id'] = self.buyer_alipay_id
        if self.equipment_name:
            if hasattr(self.equipment_name, 'to_alipay_dict'):
                params['equipment_name'] = self.equipment_name.to_alipay_dict()
            else:
                params['equipment_name'] = self.equipment_name
        if self.equipment_no:
            if hasattr(self.equipment_no, 'to_alipay_dict'):
                params['equipment_no'] = self.equipment_no.to_alipay_dict()
            else:
                params['equipment_no'] = self.equipment_no
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.invoice_number:
            if hasattr(self.invoice_number, 'to_alipay_dict'):
                params['invoice_number'] = self.invoice_number.to_alipay_dict()
            else:
                params['invoice_number'] = self.invoice_number
        if self.logistics_order_no:
            if hasattr(self.logistics_order_no, 'to_alipay_dict'):
                params['logistics_order_no'] = self.logistics_order_no.to_alipay_dict()
            else:
                params['logistics_order_no'] = self.logistics_order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.preauth_freeze_time:
            if hasattr(self.preauth_freeze_time, 'to_alipay_dict'):
                params['preauth_freeze_time'] = self.preauth_freeze_time.to_alipay_dict()
            else:
                params['preauth_freeze_time'] = self.preauth_freeze_time
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_no:
            if hasattr(self.store_no, 'to_alipay_dict'):
                params['store_no'] = self.store_no.to_alipay_dict()
            else:
                params['store_no'] = self.store_no
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainFactoringAfterloaninfoSaveModel()
        if 'activate_state' in d:
            o.activate_state = d['activate_state']
        if 'activate_time' in d:
            o.activate_time = d['activate_time']
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'buyer_alipay_id' in d:
            o.buyer_alipay_id = d['buyer_alipay_id']
        if 'equipment_name' in d:
            o.equipment_name = d['equipment_name']
        if 'equipment_no' in d:
            o.equipment_no = d['equipment_no']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'invoice_number' in d:
            o.invoice_number = d['invoice_number']
        if 'logistics_order_no' in d:
            o.logistics_order_no = d['logistics_order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'preauth_freeze_time' in d:
            o.preauth_freeze_time = d['preauth_freeze_time']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_no' in d:
            o.store_no = d['store_no']
        if 'term' in d:
            o.term = d['term']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


