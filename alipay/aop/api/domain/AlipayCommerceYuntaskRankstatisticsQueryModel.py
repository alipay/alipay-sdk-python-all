#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskRankstatisticsQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._hunter_id = None
        self._hunter_open_id = None
        self._merchant_pid = None
        self._page = None
        self._page_size = None
        self._rank_range = None
        self._shop_id = None
        self._sort_type = None
        self._task_template_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def hunter_open_id(self):
        return self._hunter_open_id

    @hunter_open_id.setter
    def hunter_open_id(self, value):
        self._hunter_open_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def rank_range(self):
        return self._rank_range

    @rank_range.setter
    def rank_range(self, value):
        self._rank_range = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
        if self.hunter_open_id:
            if hasattr(self.hunter_open_id, 'to_alipay_dict'):
                params['hunter_open_id'] = self.hunter_open_id.to_alipay_dict()
            else:
                params['hunter_open_id'] = self.hunter_open_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.rank_range:
            if hasattr(self.rank_range, 'to_alipay_dict'):
                params['rank_range'] = self.rank_range.to_alipay_dict()
            else:
                params['rank_range'] = self.rank_range
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskRankstatisticsQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'hunter_open_id' in d:
            o.hunter_open_id = d['hunter_open_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'rank_range' in d:
            o.rank_range = d['rank_range']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


