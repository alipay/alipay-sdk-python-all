#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeRecord(object):

    def __init__(self):
        self._alipay_order_no = None
        self._create_time = None
        self._in_out_type = None
        self._merchant_order_no = None
        self._modified_time = None
        self._opposite_logon_id = None
        self._opposite_name = None
        self._opposite_user_id = None
        self._order_from = None
        self._order_status = None
        self._order_title = None
        self._order_type = None
        self._owner_logon_id = None
        self._owner_name = None
        self._owner_user_id = None
        self._partner_id = None
        self._service_charge = None
        self._total_amount = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def in_out_type(self):
        return self._in_out_type

    @in_out_type.setter
    def in_out_type(self, value):
        self._in_out_type = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def opposite_logon_id(self):
        return self._opposite_logon_id

    @opposite_logon_id.setter
    def opposite_logon_id(self, value):
        self._opposite_logon_id = value
    @property
    def opposite_name(self):
        return self._opposite_name

    @opposite_name.setter
    def opposite_name(self, value):
        self._opposite_name = value
    @property
    def opposite_user_id(self):
        return self._opposite_user_id

    @opposite_user_id.setter
    def opposite_user_id(self, value):
        self._opposite_user_id = value
    @property
    def order_from(self):
        return self._order_from

    @order_from.setter
    def order_from(self, value):
        self._order_from = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def owner_logon_id(self):
        return self._owner_logon_id

    @owner_logon_id.setter
    def owner_logon_id(self, value):
        self._owner_logon_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def owner_user_id(self):
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, value):
        self._owner_user_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def service_charge(self):
        return self._service_charge

    @service_charge.setter
    def service_charge(self, value):
        self._service_charge = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.in_out_type:
            if hasattr(self.in_out_type, 'to_alipay_dict'):
                params['in_out_type'] = self.in_out_type.to_alipay_dict()
            else:
                params['in_out_type'] = self.in_out_type
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.opposite_logon_id:
            if hasattr(self.opposite_logon_id, 'to_alipay_dict'):
                params['opposite_logon_id'] = self.opposite_logon_id.to_alipay_dict()
            else:
                params['opposite_logon_id'] = self.opposite_logon_id
        if self.opposite_name:
            if hasattr(self.opposite_name, 'to_alipay_dict'):
                params['opposite_name'] = self.opposite_name.to_alipay_dict()
            else:
                params['opposite_name'] = self.opposite_name
        if self.opposite_user_id:
            if hasattr(self.opposite_user_id, 'to_alipay_dict'):
                params['opposite_user_id'] = self.opposite_user_id.to_alipay_dict()
            else:
                params['opposite_user_id'] = self.opposite_user_id
        if self.order_from:
            if hasattr(self.order_from, 'to_alipay_dict'):
                params['order_from'] = self.order_from.to_alipay_dict()
            else:
                params['order_from'] = self.order_from
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.owner_logon_id:
            if hasattr(self.owner_logon_id, 'to_alipay_dict'):
                params['owner_logon_id'] = self.owner_logon_id.to_alipay_dict()
            else:
                params['owner_logon_id'] = self.owner_logon_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.owner_user_id:
            if hasattr(self.owner_user_id, 'to_alipay_dict'):
                params['owner_user_id'] = self.owner_user_id.to_alipay_dict()
            else:
                params['owner_user_id'] = self.owner_user_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.service_charge:
            if hasattr(self.service_charge, 'to_alipay_dict'):
                params['service_charge'] = self.service_charge.to_alipay_dict()
            else:
                params['service_charge'] = self.service_charge
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
        o = TradeRecord()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'in_out_type' in d:
            o.in_out_type = d['in_out_type']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'opposite_logon_id' in d:
            o.opposite_logon_id = d['opposite_logon_id']
        if 'opposite_name' in d:
            o.opposite_name = d['opposite_name']
        if 'opposite_user_id' in d:
            o.opposite_user_id = d['opposite_user_id']
        if 'order_from' in d:
            o.order_from = d['order_from']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'owner_logon_id' in d:
            o.owner_logon_id = d['owner_logon_id']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'owner_user_id' in d:
            o.owner_user_id = d['owner_user_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'service_charge' in d:
            o.service_charge = d['service_charge']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


