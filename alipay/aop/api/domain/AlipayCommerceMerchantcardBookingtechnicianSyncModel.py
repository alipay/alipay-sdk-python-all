#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScheduleWeekPlanInfo import ScheduleWeekPlanInfo


class AlipayCommerceMerchantcardBookingtechnicianSyncModel(object):

    def __init__(self):
        self._avatar_file_id = None
        self._career_start_month = None
        self._nick = None
        self._out_technician_id = None
        self._phone = None
        self._service_ids = None
        self._shop_id = None
        self._status = None
        self._technician_id = None
        self._title = None
        self._week_plans = None

    @property
    def avatar_file_id(self):
        return self._avatar_file_id

    @avatar_file_id.setter
    def avatar_file_id(self, value):
        self._avatar_file_id = value
    @property
    def career_start_month(self):
        return self._career_start_month

    @career_start_month.setter
    def career_start_month(self, value):
        self._career_start_month = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def out_technician_id(self):
        return self._out_technician_id

    @out_technician_id.setter
    def out_technician_id(self, value):
        self._out_technician_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def service_ids(self):
        return self._service_ids

    @service_ids.setter
    def service_ids(self, value):
        if isinstance(value, list):
            self._service_ids = list()
            for i in value:
                self._service_ids.append(i)
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
    def technician_id(self):
        return self._technician_id

    @technician_id.setter
    def technician_id(self, value):
        self._technician_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
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
        if self.avatar_file_id:
            if hasattr(self.avatar_file_id, 'to_alipay_dict'):
                params['avatar_file_id'] = self.avatar_file_id.to_alipay_dict()
            else:
                params['avatar_file_id'] = self.avatar_file_id
        if self.career_start_month:
            if hasattr(self.career_start_month, 'to_alipay_dict'):
                params['career_start_month'] = self.career_start_month.to_alipay_dict()
            else:
                params['career_start_month'] = self.career_start_month
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        if self.out_technician_id:
            if hasattr(self.out_technician_id, 'to_alipay_dict'):
                params['out_technician_id'] = self.out_technician_id.to_alipay_dict()
            else:
                params['out_technician_id'] = self.out_technician_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.service_ids:
            if isinstance(self.service_ids, list):
                for i in range(0, len(self.service_ids)):
                    element = self.service_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_ids[i] = element.to_alipay_dict()
            if hasattr(self.service_ids, 'to_alipay_dict'):
                params['service_ids'] = self.service_ids.to_alipay_dict()
            else:
                params['service_ids'] = self.service_ids
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
        if self.technician_id:
            if hasattr(self.technician_id, 'to_alipay_dict'):
                params['technician_id'] = self.technician_id.to_alipay_dict()
            else:
                params['technician_id'] = self.technician_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = AlipayCommerceMerchantcardBookingtechnicianSyncModel()
        if 'avatar_file_id' in d:
            o.avatar_file_id = d['avatar_file_id']
        if 'career_start_month' in d:
            o.career_start_month = d['career_start_month']
        if 'nick' in d:
            o.nick = d['nick']
        if 'out_technician_id' in d:
            o.out_technician_id = d['out_technician_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'service_ids' in d:
            o.service_ids = d['service_ids']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'technician_id' in d:
            o.technician_id = d['technician_id']
        if 'title' in d:
            o.title = d['title']
        if 'week_plans' in d:
            o.week_plans = d['week_plans']
        return o


