#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdAsiadReceiptCreateModel(object):

    def __init__(self):
        self._app_name = None
        self._cooperate_mode = None
        self._description = None
        self._end_time = None
        self._fault_action = None
        self._fault_effect = None
        self._fault_effect_value = None
        self._fault_handler = None
        self._fault_level = None
        self._fault_responsible = None
        self._fault_source = None
        self._fault_status = None
        self._fault_type = None
        self._project_name = None
        self._request_id = None
        self._request_key = None
        self._start_time = None
        self._tenant_name = None
        self._title = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def cooperate_mode(self):
        return self._cooperate_mode

    @cooperate_mode.setter
    def cooperate_mode(self, value):
        self._cooperate_mode = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fault_action(self):
        return self._fault_action

    @fault_action.setter
    def fault_action(self, value):
        self._fault_action = value
    @property
    def fault_effect(self):
        return self._fault_effect

    @fault_effect.setter
    def fault_effect(self, value):
        self._fault_effect = value
    @property
    def fault_effect_value(self):
        return self._fault_effect_value

    @fault_effect_value.setter
    def fault_effect_value(self, value):
        self._fault_effect_value = value
    @property
    def fault_handler(self):
        return self._fault_handler

    @fault_handler.setter
    def fault_handler(self, value):
        self._fault_handler = value
    @property
    def fault_level(self):
        return self._fault_level

    @fault_level.setter
    def fault_level(self, value):
        self._fault_level = value
    @property
    def fault_responsible(self):
        return self._fault_responsible

    @fault_responsible.setter
    def fault_responsible(self, value):
        self._fault_responsible = value
    @property
    def fault_source(self):
        return self._fault_source

    @fault_source.setter
    def fault_source(self, value):
        self._fault_source = value
    @property
    def fault_status(self):
        return self._fault_status

    @fault_status.setter
    def fault_status(self, value):
        self._fault_status = value
    @property
    def fault_type(self):
        return self._fault_type

    @fault_type.setter
    def fault_type(self, value):
        self._fault_type = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def request_key(self):
        return self._request_key

    @request_key.setter
    def request_key(self, value):
        self._request_key = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def tenant_name(self):
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, value):
        self._tenant_name = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.cooperate_mode:
            if hasattr(self.cooperate_mode, 'to_alipay_dict'):
                params['cooperate_mode'] = self.cooperate_mode.to_alipay_dict()
            else:
                params['cooperate_mode'] = self.cooperate_mode
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fault_action:
            if hasattr(self.fault_action, 'to_alipay_dict'):
                params['fault_action'] = self.fault_action.to_alipay_dict()
            else:
                params['fault_action'] = self.fault_action
        if self.fault_effect:
            if hasattr(self.fault_effect, 'to_alipay_dict'):
                params['fault_effect'] = self.fault_effect.to_alipay_dict()
            else:
                params['fault_effect'] = self.fault_effect
        if self.fault_effect_value:
            if hasattr(self.fault_effect_value, 'to_alipay_dict'):
                params['fault_effect_value'] = self.fault_effect_value.to_alipay_dict()
            else:
                params['fault_effect_value'] = self.fault_effect_value
        if self.fault_handler:
            if hasattr(self.fault_handler, 'to_alipay_dict'):
                params['fault_handler'] = self.fault_handler.to_alipay_dict()
            else:
                params['fault_handler'] = self.fault_handler
        if self.fault_level:
            if hasattr(self.fault_level, 'to_alipay_dict'):
                params['fault_level'] = self.fault_level.to_alipay_dict()
            else:
                params['fault_level'] = self.fault_level
        if self.fault_responsible:
            if hasattr(self.fault_responsible, 'to_alipay_dict'):
                params['fault_responsible'] = self.fault_responsible.to_alipay_dict()
            else:
                params['fault_responsible'] = self.fault_responsible
        if self.fault_source:
            if hasattr(self.fault_source, 'to_alipay_dict'):
                params['fault_source'] = self.fault_source.to_alipay_dict()
            else:
                params['fault_source'] = self.fault_source
        if self.fault_status:
            if hasattr(self.fault_status, 'to_alipay_dict'):
                params['fault_status'] = self.fault_status.to_alipay_dict()
            else:
                params['fault_status'] = self.fault_status
        if self.fault_type:
            if hasattr(self.fault_type, 'to_alipay_dict'):
                params['fault_type'] = self.fault_type.to_alipay_dict()
            else:
                params['fault_type'] = self.fault_type
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.request_key:
            if hasattr(self.request_key, 'to_alipay_dict'):
                params['request_key'] = self.request_key.to_alipay_dict()
            else:
                params['request_key'] = self.request_key
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.tenant_name:
            if hasattr(self.tenant_name, 'to_alipay_dict'):
                params['tenant_name'] = self.tenant_name.to_alipay_dict()
            else:
                params['tenant_name'] = self.tenant_name
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAsiadReceiptCreateModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'cooperate_mode' in d:
            o.cooperate_mode = d['cooperate_mode']
        if 'description' in d:
            o.description = d['description']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fault_action' in d:
            o.fault_action = d['fault_action']
        if 'fault_effect' in d:
            o.fault_effect = d['fault_effect']
        if 'fault_effect_value' in d:
            o.fault_effect_value = d['fault_effect_value']
        if 'fault_handler' in d:
            o.fault_handler = d['fault_handler']
        if 'fault_level' in d:
            o.fault_level = d['fault_level']
        if 'fault_responsible' in d:
            o.fault_responsible = d['fault_responsible']
        if 'fault_source' in d:
            o.fault_source = d['fault_source']
        if 'fault_status' in d:
            o.fault_status = d['fault_status']
        if 'fault_type' in d:
            o.fault_type = d['fault_type']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'request_key' in d:
            o.request_key = d['request_key']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'tenant_name' in d:
            o.tenant_name = d['tenant_name']
        if 'title' in d:
            o.title = d['title']
        return o


