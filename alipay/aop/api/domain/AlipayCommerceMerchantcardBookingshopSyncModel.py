#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScheduleWeekPlanInfo import ScheduleWeekPlanInfo


class AlipayCommerceMerchantcardBookingshopSyncModel(object):

    def __init__(self):
        self._book_interval = None
        self._book_need_confirm = None
        self._book_with_item = None
        self._book_with_service = None
        self._can_not_book_items = None
        self._max_book_count = None
        self._msg_app_id = None
        self._out_shop_id = None
        self._shop_id = None
        self._status = None
        self._stock_fetch_type = None
        self._stock_query_app_id = None
        self._week_plans = None

    @property
    def book_interval(self):
        return self._book_interval

    @book_interval.setter
    def book_interval(self, value):
        self._book_interval = value
    @property
    def book_need_confirm(self):
        return self._book_need_confirm

    @book_need_confirm.setter
    def book_need_confirm(self, value):
        self._book_need_confirm = value
    @property
    def book_with_item(self):
        return self._book_with_item

    @book_with_item.setter
    def book_with_item(self, value):
        self._book_with_item = value
    @property
    def book_with_service(self):
        return self._book_with_service

    @book_with_service.setter
    def book_with_service(self, value):
        self._book_with_service = value
    @property
    def can_not_book_items(self):
        return self._can_not_book_items

    @can_not_book_items.setter
    def can_not_book_items(self, value):
        if isinstance(value, list):
            self._can_not_book_items = list()
            for i in value:
                self._can_not_book_items.append(i)
    @property
    def max_book_count(self):
        return self._max_book_count

    @max_book_count.setter
    def max_book_count(self, value):
        self._max_book_count = value
    @property
    def msg_app_id(self):
        return self._msg_app_id

    @msg_app_id.setter
    def msg_app_id(self, value):
        self._msg_app_id = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stock_fetch_type(self):
        return self._stock_fetch_type

    @stock_fetch_type.setter
    def stock_fetch_type(self, value):
        self._stock_fetch_type = value
    @property
    def stock_query_app_id(self):
        return self._stock_query_app_id

    @stock_query_app_id.setter
    def stock_query_app_id(self, value):
        self._stock_query_app_id = value
    @property
    def week_plans(self):
        return self._week_plans

    @week_plans.setter
    def week_plans(self, value):
        if isinstance(value, list):
            self._week_plans = list()
            for i in value:
                if isinstance(i, ScheduleWeekPlanInfo):
                    self._week_plans.append(i)
                else:
                    self._week_plans.append(ScheduleWeekPlanInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.book_interval:
            if hasattr(self.book_interval, 'to_alipay_dict'):
                params['book_interval'] = self.book_interval.to_alipay_dict()
            else:
                params['book_interval'] = self.book_interval
        if self.book_need_confirm:
            if hasattr(self.book_need_confirm, 'to_alipay_dict'):
                params['book_need_confirm'] = self.book_need_confirm.to_alipay_dict()
            else:
                params['book_need_confirm'] = self.book_need_confirm
        if self.book_with_item:
            if hasattr(self.book_with_item, 'to_alipay_dict'):
                params['book_with_item'] = self.book_with_item.to_alipay_dict()
            else:
                params['book_with_item'] = self.book_with_item
        if self.book_with_service:
            if hasattr(self.book_with_service, 'to_alipay_dict'):
                params['book_with_service'] = self.book_with_service.to_alipay_dict()
            else:
                params['book_with_service'] = self.book_with_service
        if self.can_not_book_items:
            if isinstance(self.can_not_book_items, list):
                for i in range(0, len(self.can_not_book_items)):
                    element = self.can_not_book_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.can_not_book_items[i] = element.to_alipay_dict()
            if hasattr(self.can_not_book_items, 'to_alipay_dict'):
                params['can_not_book_items'] = self.can_not_book_items.to_alipay_dict()
            else:
                params['can_not_book_items'] = self.can_not_book_items
        if self.max_book_count:
            if hasattr(self.max_book_count, 'to_alipay_dict'):
                params['max_book_count'] = self.max_book_count.to_alipay_dict()
            else:
                params['max_book_count'] = self.max_book_count
        if self.msg_app_id:
            if hasattr(self.msg_app_id, 'to_alipay_dict'):
                params['msg_app_id'] = self.msg_app_id.to_alipay_dict()
            else:
                params['msg_app_id'] = self.msg_app_id
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.stock_fetch_type:
            if hasattr(self.stock_fetch_type, 'to_alipay_dict'):
                params['stock_fetch_type'] = self.stock_fetch_type.to_alipay_dict()
            else:
                params['stock_fetch_type'] = self.stock_fetch_type
        if self.stock_query_app_id:
            if hasattr(self.stock_query_app_id, 'to_alipay_dict'):
                params['stock_query_app_id'] = self.stock_query_app_id.to_alipay_dict()
            else:
                params['stock_query_app_id'] = self.stock_query_app_id
        if self.week_plans:
            if isinstance(self.week_plans, list):
                for i in range(0, len(self.week_plans)):
                    element = self.week_plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_plans[i] = element.to_alipay_dict()
            if hasattr(self.week_plans, 'to_alipay_dict'):
                params['week_plans'] = self.week_plans.to_alipay_dict()
            else:
                params['week_plans'] = self.week_plans
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardBookingshopSyncModel()
        if 'book_interval' in d:
            o.book_interval = d['book_interval']
        if 'book_need_confirm' in d:
            o.book_need_confirm = d['book_need_confirm']
        if 'book_with_item' in d:
            o.book_with_item = d['book_with_item']
        if 'book_with_service' in d:
            o.book_with_service = d['book_with_service']
        if 'can_not_book_items' in d:
            o.can_not_book_items = d['can_not_book_items']
        if 'max_book_count' in d:
            o.max_book_count = d['max_book_count']
        if 'msg_app_id' in d:
            o.msg_app_id = d['msg_app_id']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'stock_fetch_type' in d:
            o.stock_fetch_type = d['stock_fetch_type']
        if 'stock_query_app_id' in d:
            o.stock_query_app_id = d['stock_query_app_id']
        if 'week_plans' in d:
            o.week_plans = d['week_plans']
        return o


