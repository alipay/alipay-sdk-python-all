#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishTabInfo(object):

    def __init__(self):
        self._area_id = None
        self._create_user = None
        self._fee_price = None
        self._seat_count = None
        self._tab_id = None
        self._tab_name = None
        self._tab_sort = None
        self._tab_tstatus = None
        self._update_user = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def fee_price(self):
        return self._fee_price

    @fee_price.setter
    def fee_price(self, value):
        self._fee_price = value
    @property
    def seat_count(self):
        return self._seat_count

    @seat_count.setter
    def seat_count(self, value):
        self._seat_count = value
    @property
    def tab_id(self):
        return self._tab_id

    @tab_id.setter
    def tab_id(self, value):
        self._tab_id = value
    @property
    def tab_name(self):
        return self._tab_name

    @tab_name.setter
    def tab_name(self, value):
        self._tab_name = value
    @property
    def tab_sort(self):
        return self._tab_sort

    @tab_sort.setter
    def tab_sort(self, value):
        self._tab_sort = value
    @property
    def tab_tstatus(self):
        return self._tab_tstatus

    @tab_tstatus.setter
    def tab_tstatus(self, value):
        self._tab_tstatus = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.fee_price:
            if hasattr(self.fee_price, 'to_alipay_dict'):
                params['fee_price'] = self.fee_price.to_alipay_dict()
            else:
                params['fee_price'] = self.fee_price
        if self.seat_count:
            if hasattr(self.seat_count, 'to_alipay_dict'):
                params['seat_count'] = self.seat_count.to_alipay_dict()
            else:
                params['seat_count'] = self.seat_count
        if self.tab_id:
            if hasattr(self.tab_id, 'to_alipay_dict'):
                params['tab_id'] = self.tab_id.to_alipay_dict()
            else:
                params['tab_id'] = self.tab_id
        if self.tab_name:
            if hasattr(self.tab_name, 'to_alipay_dict'):
                params['tab_name'] = self.tab_name.to_alipay_dict()
            else:
                params['tab_name'] = self.tab_name
        if self.tab_sort:
            if hasattr(self.tab_sort, 'to_alipay_dict'):
                params['tab_sort'] = self.tab_sort.to_alipay_dict()
            else:
                params['tab_sort'] = self.tab_sort
        if self.tab_tstatus:
            if hasattr(self.tab_tstatus, 'to_alipay_dict'):
                params['tab_tstatus'] = self.tab_tstatus.to_alipay_dict()
            else:
                params['tab_tstatus'] = self.tab_tstatus
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishTabInfo()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'fee_price' in d:
            o.fee_price = d['fee_price']
        if 'seat_count' in d:
            o.seat_count = d['seat_count']
        if 'tab_id' in d:
            o.tab_id = d['tab_id']
        if 'tab_name' in d:
            o.tab_name = d['tab_name']
        if 'tab_sort' in d:
            o.tab_sort = d['tab_sort']
        if 'tab_tstatus' in d:
            o.tab_tstatus = d['tab_tstatus']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


