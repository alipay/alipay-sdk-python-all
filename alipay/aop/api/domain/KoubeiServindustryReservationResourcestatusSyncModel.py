#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IsvCyclePropertyTimeModel import IsvCyclePropertyTimeModel
from alipay.aop.api.domain.ReservationTimeUnit import ReservationTimeUnit
from alipay.aop.api.domain.ReservationTimeUnit import ReservationTimeUnit


class KoubeiServindustryReservationResourcestatusSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._cycle_property_time = None
        self._date = None
        self._end_time = None
        self._industry = None
        self._out_biz_id = None
        self._resource_id = None
        self._shop_id = None
        self._start_time = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        if isinstance(value, list):
            self._biz_type = list()
            for i in value:
                self._biz_type.append(i)
    @property
    def cycle_property_time(self):
        return self._cycle_property_time

    @cycle_property_time.setter
    def cycle_property_time(self, value):
        if isinstance(value, IsvCyclePropertyTimeModel):
            self._cycle_property_time = value
        else:
            self._cycle_property_time = IsvCyclePropertyTimeModel.from_alipay_dict(value)
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        if isinstance(value, ReservationTimeUnit):
            self._end_time = value
        else:
            self._end_time = ReservationTimeUnit.from_alipay_dict(value)
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        if isinstance(value, ReservationTimeUnit):
            self._start_time = value
        else:
            self._start_time = ReservationTimeUnit.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if isinstance(self.biz_type, list):
                for i in range(0, len(self.biz_type)):
                    element = self.biz_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_type[i] = element.to_alipay_dict()
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cycle_property_time:
            if hasattr(self.cycle_property_time, 'to_alipay_dict'):
                params['cycle_property_time'] = self.cycle_property_time.to_alipay_dict()
            else:
                params['cycle_property_time'] = self.cycle_property_time
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryReservationResourcestatusSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cycle_property_time' in d:
            o.cycle_property_time = d['cycle_property_time']
        if 'date' in d:
            o.date = d['date']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'industry' in d:
            o.industry = d['industry']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


