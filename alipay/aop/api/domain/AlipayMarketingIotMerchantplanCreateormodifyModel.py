#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingIotMerchantplanCreateormodifyModel(object):

    def __init__(self):
        self._action = None
        self._end_time = None
        self._merchant_plan_id = None
        self._mini_app_id = None
        self._mini_app_page = None
        self._plan_id = None
        self._resource_content = None
        self._resource_type = None
        self._space_code = None
        self._start_time = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def merchant_plan_id(self):
        return self._merchant_plan_id

    @merchant_plan_id.setter
    def merchant_plan_id(self, value):
        self._merchant_plan_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_page(self):
        return self._mini_app_page

    @mini_app_page.setter
    def mini_app_page(self, value):
        self._mini_app_page = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def resource_content(self):
        return self._resource_content

    @resource_content.setter
    def resource_content(self, value):
        self._resource_content = value
    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        self._resource_type = value
    @property
    def space_code(self):
        return self._space_code

    @space_code.setter
    def space_code(self, value):
        self._space_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.merchant_plan_id:
            if hasattr(self.merchant_plan_id, 'to_alipay_dict'):
                params['merchant_plan_id'] = self.merchant_plan_id.to_alipay_dict()
            else:
                params['merchant_plan_id'] = self.merchant_plan_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_page:
            if hasattr(self.mini_app_page, 'to_alipay_dict'):
                params['mini_app_page'] = self.mini_app_page.to_alipay_dict()
            else:
                params['mini_app_page'] = self.mini_app_page
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.resource_content:
            if hasattr(self.resource_content, 'to_alipay_dict'):
                params['resource_content'] = self.resource_content.to_alipay_dict()
            else:
                params['resource_content'] = self.resource_content
        if self.resource_type:
            if hasattr(self.resource_type, 'to_alipay_dict'):
                params['resource_type'] = self.resource_type.to_alipay_dict()
            else:
                params['resource_type'] = self.resource_type
        if self.space_code:
            if hasattr(self.space_code, 'to_alipay_dict'):
                params['space_code'] = self.space_code.to_alipay_dict()
            else:
                params['space_code'] = self.space_code
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
        o = AlipayMarketingIotMerchantplanCreateormodifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'merchant_plan_id' in d:
            o.merchant_plan_id = d['merchant_plan_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_page' in d:
            o.mini_app_page = d['mini_app_page']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'resource_content' in d:
            o.resource_content = d['resource_content']
        if 'resource_type' in d:
            o.resource_type = d['resource_type']
        if 'space_code' in d:
            o.space_code = d['space_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


