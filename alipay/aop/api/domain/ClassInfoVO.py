#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClassInfoVO(object):

    def __init__(self):
        self._biz_no = None
        self._end_date = None
        self._schedule_description = None
        self._shop_id = None
        self._start_date = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def schedule_description(self):
        return self._schedule_description

    @schedule_description.setter
    def schedule_description(self, value):
        self._schedule_description = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.schedule_description:
            if hasattr(self.schedule_description, 'to_alipay_dict'):
                params['schedule_description'] = self.schedule_description.to_alipay_dict()
            else:
                params['schedule_description'] = self.schedule_description
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClassInfoVO()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'schedule_description' in d:
            o.schedule_description = d['schedule_description']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


