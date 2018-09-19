#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryInstBillDetail import QueryInstBillDetail


class QueryInstBillInfo(object):

    def __init__(self):
        self._amount = None
        self._balance = None
        self._bill_date = None
        self._bill_detail = None
        self._bill_fines = None
        self._bill_key = None
        self._bill_user_name = None
        self._charge_inst = None
        self._charge_uniq_id = None
        self._chargeoff_inst = None
        self._company_id = None
        self._extend = None
        self._order_type = None
        self._out_id = None
        self._return_message = None
        self._sub_order_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_detail(self):
        return self._bill_detail

    @bill_detail.setter
    def bill_detail(self, value):
        if isinstance(value, list):
            self._bill_detail = list()
            for i in value:
                if isinstance(i, QueryInstBillDetail):
                    self._bill_detail.append(i)
                else:
                    self._bill_detail.append(QueryInstBillDetail.from_alipay_dict(i))
    @property
    def bill_fines(self):
        return self._bill_fines

    @bill_fines.setter
    def bill_fines(self, value):
        self._bill_fines = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def bill_user_name(self):
        return self._bill_user_name

    @bill_user_name.setter
    def bill_user_name(self, value):
        self._bill_user_name = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def charge_uniq_id(self):
        return self._charge_uniq_id

    @charge_uniq_id.setter
    def charge_uniq_id(self, value):
        self._charge_uniq_id = value
    @property
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def return_message(self):
        return self._return_message

    @return_message.setter
    def return_message(self, value):
        self._return_message = value
    @property
    def sub_order_type(self):
        return self._sub_order_type

    @sub_order_type.setter
    def sub_order_type(self, value):
        self._sub_order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_detail:
            if isinstance(self.bill_detail, list):
                for i in range(0, len(self.bill_detail)):
                    element = self.bill_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_detail[i] = element.to_alipay_dict()
            if hasattr(self.bill_detail, 'to_alipay_dict'):
                params['bill_detail'] = self.bill_detail.to_alipay_dict()
            else:
                params['bill_detail'] = self.bill_detail
        if self.bill_fines:
            if hasattr(self.bill_fines, 'to_alipay_dict'):
                params['bill_fines'] = self.bill_fines.to_alipay_dict()
            else:
                params['bill_fines'] = self.bill_fines
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.bill_user_name:
            if hasattr(self.bill_user_name, 'to_alipay_dict'):
                params['bill_user_name'] = self.bill_user_name.to_alipay_dict()
            else:
                params['bill_user_name'] = self.bill_user_name
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.charge_uniq_id:
            if hasattr(self.charge_uniq_id, 'to_alipay_dict'):
                params['charge_uniq_id'] = self.charge_uniq_id.to_alipay_dict()
            else:
                params['charge_uniq_id'] = self.charge_uniq_id
        if self.chargeoff_inst:
            if hasattr(self.chargeoff_inst, 'to_alipay_dict'):
                params['chargeoff_inst'] = self.chargeoff_inst.to_alipay_dict()
            else:
                params['chargeoff_inst'] = self.chargeoff_inst
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.return_message:
            if hasattr(self.return_message, 'to_alipay_dict'):
                params['return_message'] = self.return_message.to_alipay_dict()
            else:
                params['return_message'] = self.return_message
        if self.sub_order_type:
            if hasattr(self.sub_order_type, 'to_alipay_dict'):
                params['sub_order_type'] = self.sub_order_type.to_alipay_dict()
            else:
                params['sub_order_type'] = self.sub_order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryInstBillInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'balance' in d:
            o.balance = d['balance']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_detail' in d:
            o.bill_detail = d['bill_detail']
        if 'bill_fines' in d:
            o.bill_fines = d['bill_fines']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'bill_user_name' in d:
            o.bill_user_name = d['bill_user_name']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'charge_uniq_id' in d:
            o.charge_uniq_id = d['charge_uniq_id']
        if 'chargeoff_inst' in d:
            o.chargeoff_inst = d['chargeoff_inst']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'extend' in d:
            o.extend = d['extend']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'return_message' in d:
            o.return_message = d['return_message']
        if 'sub_order_type' in d:
            o.sub_order_type = d['sub_order_type']
        return o


