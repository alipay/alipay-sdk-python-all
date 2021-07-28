#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishCategorySimplifyInfo import KbdishCategorySimplifyInfo


class KoubeiCateringDishMenuQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishMenuQueryResponse, self).__init__()
        self._bg_image = None
        self._category_list = None
        self._cook_name = None
        self._end_date = None
        self._end_time = None
        self._out_shop_id = None
        self._period_type = None
        self._period_value = None
        self._start_date = None
        self._start_time = None
        self._status = None

    @property
    def bg_image(self):
        return self._bg_image

    @bg_image.setter
    def bg_image(self, value):
        self._bg_image = value
    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, KbdishCategorySimplifyInfo):
            self._category_list = value
        else:
            self._category_list = KbdishCategorySimplifyInfo.from_alipay_dict(value)
    @property
    def cook_name(self):
        return self._cook_name

    @cook_name.setter
    def cook_name(self, value):
        self._cook_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        if isinstance(value, list):
            self._out_shop_id = list()
            for i in value:
                self._out_shop_id.append(i)
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def period_value(self):
        return self._period_value

    @period_value.setter
    def period_value(self, value):
        self._period_value = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishMenuQueryResponse, self).parse_response_content(response_content)
        if 'bg_image' in response:
            self.bg_image = response['bg_image']
        if 'category_list' in response:
            self.category_list = response['category_list']
        if 'cook_name' in response:
            self.cook_name = response['cook_name']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'out_shop_id' in response:
            self.out_shop_id = response['out_shop_id']
        if 'period_type' in response:
            self.period_type = response['period_type']
        if 'period_value' in response:
            self.period_value = response['period_value']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
