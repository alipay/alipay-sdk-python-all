#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditmerchantProductorderSignModel(object):

    def __init__(self):
        self._category = None
        self._due_type = None
        self._from_app = None
        self._inactive_datetime = None
        self._industry = None
        self._ordered_channel = None
        self._ordered_system_code = None
        self._out_merchant_id = None
        self._pid = None
        self._ps_code = None
        self._shop_name = None
        self._shop_type = None
        self._sign_scene = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def due_type(self):
        return self._due_type

    @due_type.setter
    def due_type(self, value):
        self._due_type = value
    @property
    def from_app(self):
        return self._from_app

    @from_app.setter
    def from_app(self, value):
        self._from_app = value
    @property
    def inactive_datetime(self):
        return self._inactive_datetime

    @inactive_datetime.setter
    def inactive_datetime(self, value):
        self._inactive_datetime = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def ordered_channel(self):
        return self._ordered_channel

    @ordered_channel.setter
    def ordered_channel(self, value):
        self._ordered_channel = value
    @property
    def ordered_system_code(self):
        return self._ordered_system_code

    @ordered_system_code.setter
    def ordered_system_code(self, value):
        self._ordered_system_code = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def ps_code(self):
        return self._ps_code

    @ps_code.setter
    def ps_code(self, value):
        self._ps_code = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.due_type:
            if hasattr(self.due_type, 'to_alipay_dict'):
                params['due_type'] = self.due_type.to_alipay_dict()
            else:
                params['due_type'] = self.due_type
        if self.from_app:
            if hasattr(self.from_app, 'to_alipay_dict'):
                params['from_app'] = self.from_app.to_alipay_dict()
            else:
                params['from_app'] = self.from_app
        if self.inactive_datetime:
            if hasattr(self.inactive_datetime, 'to_alipay_dict'):
                params['inactive_datetime'] = self.inactive_datetime.to_alipay_dict()
            else:
                params['inactive_datetime'] = self.inactive_datetime
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.ordered_channel:
            if hasattr(self.ordered_channel, 'to_alipay_dict'):
                params['ordered_channel'] = self.ordered_channel.to_alipay_dict()
            else:
                params['ordered_channel'] = self.ordered_channel
        if self.ordered_system_code:
            if hasattr(self.ordered_system_code, 'to_alipay_dict'):
                params['ordered_system_code'] = self.ordered_system_code.to_alipay_dict()
            else:
                params['ordered_system_code'] = self.ordered_system_code
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.ps_code:
            if hasattr(self.ps_code, 'to_alipay_dict'):
                params['ps_code'] = self.ps_code.to_alipay_dict()
            else:
                params['ps_code'] = self.ps_code
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditmerchantProductorderSignModel()
        if 'category' in d:
            o.category = d['category']
        if 'due_type' in d:
            o.due_type = d['due_type']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'inactive_datetime' in d:
            o.inactive_datetime = d['inactive_datetime']
        if 'industry' in d:
            o.industry = d['industry']
        if 'ordered_channel' in d:
            o.ordered_channel = d['ordered_channel']
        if 'ordered_system_code' in d:
            o.ordered_system_code = d['ordered_system_code']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'ps_code' in d:
            o.ps_code = d['ps_code']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        return o


