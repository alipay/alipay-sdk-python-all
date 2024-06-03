#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExpenseBillItem(object):

    def __init__(self):
        self._account_id = None
        self._account_name = None
        self._account_open_id = None
        self._amount = None
        self._charge_ou = None
        self._direction = None
        self._occurrence_time = None
        self._product_code = None
        self._product_name = None
        self._serial_no = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_open_id(self):
        return self._account_open_id

    @account_open_id.setter
    def account_open_id(self, value):
        self._account_open_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def charge_ou(self):
        return self._charge_ou

    @charge_ou.setter
    def charge_ou(self, value):
        self._charge_ou = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def occurrence_time(self):
        return self._occurrence_time

    @occurrence_time.setter
    def occurrence_time(self, value):
        self._occurrence_time = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_open_id:
            if hasattr(self.account_open_id, 'to_alipay_dict'):
                params['account_open_id'] = self.account_open_id.to_alipay_dict()
            else:
                params['account_open_id'] = self.account_open_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.charge_ou:
            if hasattr(self.charge_ou, 'to_alipay_dict'):
                params['charge_ou'] = self.charge_ou.to_alipay_dict()
            else:
                params['charge_ou'] = self.charge_ou
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.occurrence_time:
            if hasattr(self.occurrence_time, 'to_alipay_dict'):
                params['occurrence_time'] = self.occurrence_time.to_alipay_dict()
            else:
                params['occurrence_time'] = self.occurrence_time
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseBillItem()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_open_id' in d:
            o.account_open_id = d['account_open_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'charge_ou' in d:
            o.charge_ou = d['charge_ou']
        if 'direction' in d:
            o.direction = d['direction']
        if 'occurrence_time' in d:
            o.occurrence_time = d['occurrence_time']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


