#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DmActivityShopData(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._one_day_click_persons = None
        self._one_day_click_times = None
        self._one_day_exposure_times = None
        self._shop_id = None
        self._total_click_persons = None
        self._total_click_times = None
        self._total_exposure_times = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def one_day_click_persons(self):
        return self._one_day_click_persons

    @one_day_click_persons.setter
    def one_day_click_persons(self, value):
        self._one_day_click_persons = value
    @property
    def one_day_click_times(self):
        return self._one_day_click_times

    @one_day_click_times.setter
    def one_day_click_times(self, value):
        self._one_day_click_times = value
    @property
    def one_day_exposure_times(self):
        return self._one_day_exposure_times

    @one_day_exposure_times.setter
    def one_day_exposure_times(self, value):
        self._one_day_exposure_times = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def total_click_persons(self):
        return self._total_click_persons

    @total_click_persons.setter
    def total_click_persons(self, value):
        self._total_click_persons = value
    @property
    def total_click_times(self):
        return self._total_click_times

    @total_click_times.setter
    def total_click_times(self, value):
        self._total_click_times = value
    @property
    def total_exposure_times(self):
        return self._total_exposure_times

    @total_exposure_times.setter
    def total_exposure_times(self, value):
        self._total_exposure_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.one_day_click_persons:
            if hasattr(self.one_day_click_persons, 'to_alipay_dict'):
                params['one_day_click_persons'] = self.one_day_click_persons.to_alipay_dict()
            else:
                params['one_day_click_persons'] = self.one_day_click_persons
        if self.one_day_click_times:
            if hasattr(self.one_day_click_times, 'to_alipay_dict'):
                params['one_day_click_times'] = self.one_day_click_times.to_alipay_dict()
            else:
                params['one_day_click_times'] = self.one_day_click_times
        if self.one_day_exposure_times:
            if hasattr(self.one_day_exposure_times, 'to_alipay_dict'):
                params['one_day_exposure_times'] = self.one_day_exposure_times.to_alipay_dict()
            else:
                params['one_day_exposure_times'] = self.one_day_exposure_times
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.total_click_persons:
            if hasattr(self.total_click_persons, 'to_alipay_dict'):
                params['total_click_persons'] = self.total_click_persons.to_alipay_dict()
            else:
                params['total_click_persons'] = self.total_click_persons
        if self.total_click_times:
            if hasattr(self.total_click_times, 'to_alipay_dict'):
                params['total_click_times'] = self.total_click_times.to_alipay_dict()
            else:
                params['total_click_times'] = self.total_click_times
        if self.total_exposure_times:
            if hasattr(self.total_exposure_times, 'to_alipay_dict'):
                params['total_exposure_times'] = self.total_exposure_times.to_alipay_dict()
            else:
                params['total_exposure_times'] = self.total_exposure_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DmActivityShopData()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'one_day_click_persons' in d:
            o.one_day_click_persons = d['one_day_click_persons']
        if 'one_day_click_times' in d:
            o.one_day_click_times = d['one_day_click_times']
        if 'one_day_exposure_times' in d:
            o.one_day_exposure_times = d['one_day_exposure_times']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'total_click_persons' in d:
            o.total_click_persons = d['total_click_persons']
        if 'total_click_times' in d:
            o.total_click_times = d['total_click_times']
        if 'total_exposure_times' in d:
            o.total_exposure_times = d['total_exposure_times']
        return o


