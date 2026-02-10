#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr
from alipay.aop.api.domain.ScheduleWeekPlanInfo import ScheduleWeekPlanInfo


class AlipayCommerceLifeserviceShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceShopQueryResponse, self).__init__()
        self._book_interval = None
        self._book_need_confirm = None
        self._max_book_count = None
        self._msg_app_id = None
        self._out_shop_id = None
        self._shop_attrs = None
        self._shop_id = None
        self._shop_type = None
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
    def shop_attrs(self):
        return self._shop_attrs

    @shop_attrs.setter
    def shop_attrs(self, value):
        if isinstance(value, list):
            self._shop_attrs = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._shop_attrs.append(i)
                else:
                    self._shop_attrs.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceShopQueryResponse, self).parse_response_content(response_content)
        if 'book_interval' in response:
            self.book_interval = response['book_interval']
        if 'book_need_confirm' in response:
            self.book_need_confirm = response['book_need_confirm']
        if 'max_book_count' in response:
            self.max_book_count = response['max_book_count']
        if 'msg_app_id' in response:
            self.msg_app_id = response['msg_app_id']
        if 'out_shop_id' in response:
            self.out_shop_id = response['out_shop_id']
        if 'shop_attrs' in response:
            self.shop_attrs = response['shop_attrs']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_type' in response:
            self.shop_type = response['shop_type']
        if 'status' in response:
            self.status = response['status']
        if 'stock_fetch_type' in response:
            self.stock_fetch_type = response['stock_fetch_type']
        if 'stock_query_app_id' in response:
            self.stock_query_app_id = response['stock_query_app_id']
        if 'week_plans' in response:
            self.week_plans = response['week_plans']
