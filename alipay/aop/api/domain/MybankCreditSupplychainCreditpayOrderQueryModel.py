#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpayOrderQueryModel(object):

    def __init__(self):
        self._custom_info = None
        self._end_date = None
        self._items_per_page = None
        self._page = None
        self._plan_id = None
        self._start_date = None
        self._status = None
        self._trade_source = None

    @property
    def custom_info(self):
        return self._custom_info

    @custom_info.setter
    def custom_info(self, value):
        if isinstance(value, Member):
            self._custom_info = value
        else:
            self._custom_info = Member.from_alipay_dict(value)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_source(self):
        return self._trade_source

    @trade_source.setter
    def trade_source(self, value):
        self._trade_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_info:
            if hasattr(self.custom_info, 'to_alipay_dict'):
                params['custom_info'] = self.custom_info.to_alipay_dict()
            else:
                params['custom_info'] = self.custom_info
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.items_per_page:
            if hasattr(self.items_per_page, 'to_alipay_dict'):
                params['items_per_page'] = self.items_per_page.to_alipay_dict()
            else:
                params['items_per_page'] = self.items_per_page
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_source:
            if hasattr(self.trade_source, 'to_alipay_dict'):
                params['trade_source'] = self.trade_source.to_alipay_dict()
            else:
                params['trade_source'] = self.trade_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainCreditpayOrderQueryModel()
        if 'custom_info' in d:
            o.custom_info = d['custom_info']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'items_per_page' in d:
            o.items_per_page = d['items_per_page']
        if 'page' in d:
            o.page = d['page']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'trade_source' in d:
            o.trade_source = d['trade_source']
        return o


