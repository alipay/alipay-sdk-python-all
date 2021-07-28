#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoAutoaftermarketDepotCreateormodifyModel(object):

    def __init__(self):
        self._action_type = None
        self._business_end_time = None
        self._business_start_time = None
        self._calendars = None
        self._depot_account = None
        self._depot_address = None
        self._depot_id = None
        self._depot_name = None
        self._extra = None
        self._phone = None
        self._repair_scope = None
        self._threshold = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def business_end_time(self):
        return self._business_end_time

    @business_end_time.setter
    def business_end_time(self, value):
        self._business_end_time = value
    @property
    def business_start_time(self):
        return self._business_start_time

    @business_start_time.setter
    def business_start_time(self, value):
        self._business_start_time = value
    @property
    def calendars(self):
        return self._calendars

    @calendars.setter
    def calendars(self, value):
        if isinstance(value, list):
            self._calendars = list()
            for i in value:
                self._calendars.append(i)
    @property
    def depot_account(self):
        return self._depot_account

    @depot_account.setter
    def depot_account(self, value):
        self._depot_account = value
    @property
    def depot_address(self):
        return self._depot_address

    @depot_address.setter
    def depot_address(self, value):
        self._depot_address = value
    @property
    def depot_id(self):
        return self._depot_id

    @depot_id.setter
    def depot_id(self, value):
        self._depot_id = value
    @property
    def depot_name(self):
        return self._depot_name

    @depot_name.setter
    def depot_name(self, value):
        self._depot_name = value
    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        self._extra = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def repair_scope(self):
        return self._repair_scope

    @repair_scope.setter
    def repair_scope(self, value):
        self._repair_scope = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.business_end_time:
            if hasattr(self.business_end_time, 'to_alipay_dict'):
                params['business_end_time'] = self.business_end_time.to_alipay_dict()
            else:
                params['business_end_time'] = self.business_end_time
        if self.business_start_time:
            if hasattr(self.business_start_time, 'to_alipay_dict'):
                params['business_start_time'] = self.business_start_time.to_alipay_dict()
            else:
                params['business_start_time'] = self.business_start_time
        if self.calendars:
            if isinstance(self.calendars, list):
                for i in range(0, len(self.calendars)):
                    element = self.calendars[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.calendars[i] = element.to_alipay_dict()
            if hasattr(self.calendars, 'to_alipay_dict'):
                params['calendars'] = self.calendars.to_alipay_dict()
            else:
                params['calendars'] = self.calendars
        if self.depot_account:
            if hasattr(self.depot_account, 'to_alipay_dict'):
                params['depot_account'] = self.depot_account.to_alipay_dict()
            else:
                params['depot_account'] = self.depot_account
        if self.depot_address:
            if hasattr(self.depot_address, 'to_alipay_dict'):
                params['depot_address'] = self.depot_address.to_alipay_dict()
            else:
                params['depot_address'] = self.depot_address
        if self.depot_id:
            if hasattr(self.depot_id, 'to_alipay_dict'):
                params['depot_id'] = self.depot_id.to_alipay_dict()
            else:
                params['depot_id'] = self.depot_id
        if self.depot_name:
            if hasattr(self.depot_name, 'to_alipay_dict'):
                params['depot_name'] = self.depot_name.to_alipay_dict()
            else:
                params['depot_name'] = self.depot_name
        if self.extra:
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.repair_scope:
            if hasattr(self.repair_scope, 'to_alipay_dict'):
                params['repair_scope'] = self.repair_scope.to_alipay_dict()
            else:
                params['repair_scope'] = self.repair_scope
        if self.threshold:
            if hasattr(self.threshold, 'to_alipay_dict'):
                params['threshold'] = self.threshold.to_alipay_dict()
            else:
                params['threshold'] = self.threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoaftermarketDepotCreateormodifyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'business_end_time' in d:
            o.business_end_time = d['business_end_time']
        if 'business_start_time' in d:
            o.business_start_time = d['business_start_time']
        if 'calendars' in d:
            o.calendars = d['calendars']
        if 'depot_account' in d:
            o.depot_account = d['depot_account']
        if 'depot_address' in d:
            o.depot_address = d['depot_address']
        if 'depot_id' in d:
            o.depot_id = d['depot_id']
        if 'depot_name' in d:
            o.depot_name = d['depot_name']
        if 'extra' in d:
            o.extra = d['extra']
        if 'phone' in d:
            o.phone = d['phone']
        if 'repair_scope' in d:
            o.repair_scope = d['repair_scope']
        if 'threshold' in d:
            o.threshold = d['threshold']
        return o


