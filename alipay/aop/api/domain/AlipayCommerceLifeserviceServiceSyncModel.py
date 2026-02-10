#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr
from alipay.aop.api.domain.ScheduleWeekPlanInfo import ScheduleWeekPlanInfo


class AlipayCommerceLifeserviceServiceSyncModel(object):

    def __init__(self):
        self._book_with_technician = None
        self._fulfillment_type = None
        self._out_service_id = None
        self._service_attrs = None
        self._service_id = None
        self._service_name = None
        self._shop_id = None
        self._status = None
        self._week_plans = None

    @property
    def book_with_technician(self):
        return self._book_with_technician

    @book_with_technician.setter
    def book_with_technician(self, value):
        self._book_with_technician = value
    @property
    def fulfillment_type(self):
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, value):
        self._fulfillment_type = value
    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def service_attrs(self):
        return self._service_attrs

    @service_attrs.setter
    def service_attrs(self, value):
        if isinstance(value, list):
            self._service_attrs = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._service_attrs.append(i)
                else:
                    self._service_attrs.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
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
        if self.book_with_technician:
            if hasattr(self.book_with_technician, 'to_alipay_dict'):
                params['book_with_technician'] = self.book_with_technician.to_alipay_dict()
            else:
                params['book_with_technician'] = self.book_with_technician
        if self.fulfillment_type:
            if hasattr(self.fulfillment_type, 'to_alipay_dict'):
                params['fulfillment_type'] = self.fulfillment_type.to_alipay_dict()
            else:
                params['fulfillment_type'] = self.fulfillment_type
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.service_attrs:
            if isinstance(self.service_attrs, list):
                for i in range(0, len(self.service_attrs)):
                    element = self.service_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_attrs[i] = element.to_alipay_dict()
            if hasattr(self.service_attrs, 'to_alipay_dict'):
                params['service_attrs'] = self.service_attrs.to_alipay_dict()
            else:
                params['service_attrs'] = self.service_attrs
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
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
        o = AlipayCommerceLifeserviceServiceSyncModel()
        if 'book_with_technician' in d:
            o.book_with_technician = d['book_with_technician']
        if 'fulfillment_type' in d:
            o.fulfillment_type = d['fulfillment_type']
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'service_attrs' in d:
            o.service_attrs = d['service_attrs']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'week_plans' in d:
            o.week_plans = d['week_plans']
        return o


