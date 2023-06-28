#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StatementDetaileds(object):

    def __init__(self):
        self._adjust_days_quantity = None
        self._asset_id = None
        self._bill_days_quantity = None
        self._bill_end_date = None
        self._bill_start_date = None
        self._daily_contract_price = None
        self._enter_time = None
        self._exit_time = None
        self._freight_contract_price = None
        self._maintenance_amount = None
        self._month_contract_price = None
        self._real_days_quantity = None
        self._receivable_freight = None
        self._refit_amount = None
        self._rent_amount = None
        self._summary_amount = None

    @property
    def adjust_days_quantity(self):
        return self._adjust_days_quantity

    @adjust_days_quantity.setter
    def adjust_days_quantity(self, value):
        self._adjust_days_quantity = value
    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def bill_days_quantity(self):
        return self._bill_days_quantity

    @bill_days_quantity.setter
    def bill_days_quantity(self, value):
        self._bill_days_quantity = value
    @property
    def bill_end_date(self):
        return self._bill_end_date

    @bill_end_date.setter
    def bill_end_date(self, value):
        self._bill_end_date = value
    @property
    def bill_start_date(self):
        return self._bill_start_date

    @bill_start_date.setter
    def bill_start_date(self, value):
        self._bill_start_date = value
    @property
    def daily_contract_price(self):
        return self._daily_contract_price

    @daily_contract_price.setter
    def daily_contract_price(self, value):
        self._daily_contract_price = value
    @property
    def enter_time(self):
        return self._enter_time

    @enter_time.setter
    def enter_time(self, value):
        self._enter_time = value
    @property
    def exit_time(self):
        return self._exit_time

    @exit_time.setter
    def exit_time(self, value):
        self._exit_time = value
    @property
    def freight_contract_price(self):
        return self._freight_contract_price

    @freight_contract_price.setter
    def freight_contract_price(self, value):
        self._freight_contract_price = value
    @property
    def maintenance_amount(self):
        return self._maintenance_amount

    @maintenance_amount.setter
    def maintenance_amount(self, value):
        self._maintenance_amount = value
    @property
    def month_contract_price(self):
        return self._month_contract_price

    @month_contract_price.setter
    def month_contract_price(self, value):
        self._month_contract_price = value
    @property
    def real_days_quantity(self):
        return self._real_days_quantity

    @real_days_quantity.setter
    def real_days_quantity(self, value):
        self._real_days_quantity = value
    @property
    def receivable_freight(self):
        return self._receivable_freight

    @receivable_freight.setter
    def receivable_freight(self, value):
        self._receivable_freight = value
    @property
    def refit_amount(self):
        return self._refit_amount

    @refit_amount.setter
    def refit_amount(self, value):
        self._refit_amount = value
    @property
    def rent_amount(self):
        return self._rent_amount

    @rent_amount.setter
    def rent_amount(self, value):
        self._rent_amount = value
    @property
    def summary_amount(self):
        return self._summary_amount

    @summary_amount.setter
    def summary_amount(self, value):
        self._summary_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_days_quantity:
            if hasattr(self.adjust_days_quantity, 'to_alipay_dict'):
                params['adjust_days_quantity'] = self.adjust_days_quantity.to_alipay_dict()
            else:
                params['adjust_days_quantity'] = self.adjust_days_quantity
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.bill_days_quantity:
            if hasattr(self.bill_days_quantity, 'to_alipay_dict'):
                params['bill_days_quantity'] = self.bill_days_quantity.to_alipay_dict()
            else:
                params['bill_days_quantity'] = self.bill_days_quantity
        if self.bill_end_date:
            if hasattr(self.bill_end_date, 'to_alipay_dict'):
                params['bill_end_date'] = self.bill_end_date.to_alipay_dict()
            else:
                params['bill_end_date'] = self.bill_end_date
        if self.bill_start_date:
            if hasattr(self.bill_start_date, 'to_alipay_dict'):
                params['bill_start_date'] = self.bill_start_date.to_alipay_dict()
            else:
                params['bill_start_date'] = self.bill_start_date
        if self.daily_contract_price:
            if hasattr(self.daily_contract_price, 'to_alipay_dict'):
                params['daily_contract_price'] = self.daily_contract_price.to_alipay_dict()
            else:
                params['daily_contract_price'] = self.daily_contract_price
        if self.enter_time:
            if hasattr(self.enter_time, 'to_alipay_dict'):
                params['enter_time'] = self.enter_time.to_alipay_dict()
            else:
                params['enter_time'] = self.enter_time
        if self.exit_time:
            if hasattr(self.exit_time, 'to_alipay_dict'):
                params['exit_time'] = self.exit_time.to_alipay_dict()
            else:
                params['exit_time'] = self.exit_time
        if self.freight_contract_price:
            if hasattr(self.freight_contract_price, 'to_alipay_dict'):
                params['freight_contract_price'] = self.freight_contract_price.to_alipay_dict()
            else:
                params['freight_contract_price'] = self.freight_contract_price
        if self.maintenance_amount:
            if hasattr(self.maintenance_amount, 'to_alipay_dict'):
                params['maintenance_amount'] = self.maintenance_amount.to_alipay_dict()
            else:
                params['maintenance_amount'] = self.maintenance_amount
        if self.month_contract_price:
            if hasattr(self.month_contract_price, 'to_alipay_dict'):
                params['month_contract_price'] = self.month_contract_price.to_alipay_dict()
            else:
                params['month_contract_price'] = self.month_contract_price
        if self.real_days_quantity:
            if hasattr(self.real_days_quantity, 'to_alipay_dict'):
                params['real_days_quantity'] = self.real_days_quantity.to_alipay_dict()
            else:
                params['real_days_quantity'] = self.real_days_quantity
        if self.receivable_freight:
            if hasattr(self.receivable_freight, 'to_alipay_dict'):
                params['receivable_freight'] = self.receivable_freight.to_alipay_dict()
            else:
                params['receivable_freight'] = self.receivable_freight
        if self.refit_amount:
            if hasattr(self.refit_amount, 'to_alipay_dict'):
                params['refit_amount'] = self.refit_amount.to_alipay_dict()
            else:
                params['refit_amount'] = self.refit_amount
        if self.rent_amount:
            if hasattr(self.rent_amount, 'to_alipay_dict'):
                params['rent_amount'] = self.rent_amount.to_alipay_dict()
            else:
                params['rent_amount'] = self.rent_amount
        if self.summary_amount:
            if hasattr(self.summary_amount, 'to_alipay_dict'):
                params['summary_amount'] = self.summary_amount.to_alipay_dict()
            else:
                params['summary_amount'] = self.summary_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StatementDetaileds()
        if 'adjust_days_quantity' in d:
            o.adjust_days_quantity = d['adjust_days_quantity']
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'bill_days_quantity' in d:
            o.bill_days_quantity = d['bill_days_quantity']
        if 'bill_end_date' in d:
            o.bill_end_date = d['bill_end_date']
        if 'bill_start_date' in d:
            o.bill_start_date = d['bill_start_date']
        if 'daily_contract_price' in d:
            o.daily_contract_price = d['daily_contract_price']
        if 'enter_time' in d:
            o.enter_time = d['enter_time']
        if 'exit_time' in d:
            o.exit_time = d['exit_time']
        if 'freight_contract_price' in d:
            o.freight_contract_price = d['freight_contract_price']
        if 'maintenance_amount' in d:
            o.maintenance_amount = d['maintenance_amount']
        if 'month_contract_price' in d:
            o.month_contract_price = d['month_contract_price']
        if 'real_days_quantity' in d:
            o.real_days_quantity = d['real_days_quantity']
        if 'receivable_freight' in d:
            o.receivable_freight = d['receivable_freight']
        if 'refit_amount' in d:
            o.refit_amount = d['refit_amount']
        if 'rent_amount' in d:
            o.rent_amount = d['rent_amount']
        if 'summary_amount' in d:
            o.summary_amount = d['summary_amount']
        return o


