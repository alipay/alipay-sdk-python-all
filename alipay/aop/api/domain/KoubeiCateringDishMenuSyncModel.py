#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCategorySimplifyInfo import KbdishCategorySimplifyInfo


class KoubeiCateringDishMenuSyncModel(object):

    def __init__(self):
        self._bg_image = None
        self._biz_type = None
        self._category_list = None
        self._cook_name = None
        self._end_date = None
        self._end_time = None
        self._operator = None
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
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, KbdishCategorySimplifyInfo):
                    self._category_list.append(i)
                else:
                    self._category_list.append(KbdishCategorySimplifyInfo.from_alipay_dict(i))
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
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bg_image:
            if hasattr(self.bg_image, 'to_alipay_dict'):
                params['bg_image'] = self.bg_image.to_alipay_dict()
            else:
                params['bg_image'] = self.bg_image
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.category_list:
            if isinstance(self.category_list, list):
                for i in range(0, len(self.category_list)):
                    element = self.category_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_list[i] = element.to_alipay_dict()
            if hasattr(self.category_list, 'to_alipay_dict'):
                params['category_list'] = self.category_list.to_alipay_dict()
            else:
                params['category_list'] = self.category_list
        if self.cook_name:
            if hasattr(self.cook_name, 'to_alipay_dict'):
                params['cook_name'] = self.cook_name.to_alipay_dict()
            else:
                params['cook_name'] = self.cook_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_shop_id:
            if isinstance(self.out_shop_id, list):
                for i in range(0, len(self.out_shop_id)):
                    element = self.out_shop_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_shop_id[i] = element.to_alipay_dict()
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.period_value:
            if hasattr(self.period_value, 'to_alipay_dict'):
                params['period_value'] = self.period_value.to_alipay_dict()
            else:
                params['period_value'] = self.period_value
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishMenuSyncModel()
        if 'bg_image' in d:
            o.bg_image = d['bg_image']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'category_list' in d:
            o.category_list = d['category_list']
        if 'cook_name' in d:
            o.cook_name = d['cook_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'period_value' in d:
            o.period_value = d['period_value']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


