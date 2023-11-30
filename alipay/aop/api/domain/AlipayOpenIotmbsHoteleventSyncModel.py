#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsHoteleventSyncModel(object):

    def __init__(self):
        self._event_config = None
        self._event_type = None
        self._ftoken = None
        self._page = None
        self._target_app_id = None

    @property
    def event_config(self):
        return self._event_config

    @event_config.setter
    def event_config(self, value):
        self._event_config = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def target_app_id(self):
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, value):
        self._target_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_config:
            if hasattr(self.event_config, 'to_alipay_dict'):
                params['event_config'] = self.event_config.to_alipay_dict()
            else:
                params['event_config'] = self.event_config
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.target_app_id:
            if hasattr(self.target_app_id, 'to_alipay_dict'):
                params['target_app_id'] = self.target_app_id.to_alipay_dict()
            else:
                params['target_app_id'] = self.target_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsHoteleventSyncModel()
        if 'event_config' in d:
            o.event_config = d['event_config']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'page' in d:
            o.page = d['page']
        if 'target_app_id' in d:
            o.target_app_id = d['target_app_id']
        return o


