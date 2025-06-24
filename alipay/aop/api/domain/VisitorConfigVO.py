#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VisitorConfigVO(object):

    def __init__(self):
        self._entrance_open_config = None
        self._entrance_open_type = None
        self._need_owner_check = None
        self._owner_check_config = None
        self._owner_check_type = None
        self._support_open = None
        self._template_id = None

    @property
    def entrance_open_config(self):
        return self._entrance_open_config

    @entrance_open_config.setter
    def entrance_open_config(self, value):
        self._entrance_open_config = value
    @property
    def entrance_open_type(self):
        return self._entrance_open_type

    @entrance_open_type.setter
    def entrance_open_type(self, value):
        self._entrance_open_type = value
    @property
    def need_owner_check(self):
        return self._need_owner_check

    @need_owner_check.setter
    def need_owner_check(self, value):
        self._need_owner_check = value
    @property
    def owner_check_config(self):
        return self._owner_check_config

    @owner_check_config.setter
    def owner_check_config(self, value):
        self._owner_check_config = value
    @property
    def owner_check_type(self):
        return self._owner_check_type

    @owner_check_type.setter
    def owner_check_type(self, value):
        self._owner_check_type = value
    @property
    def support_open(self):
        return self._support_open

    @support_open.setter
    def support_open(self, value):
        self._support_open = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.entrance_open_config:
            if hasattr(self.entrance_open_config, 'to_alipay_dict'):
                params['entrance_open_config'] = self.entrance_open_config.to_alipay_dict()
            else:
                params['entrance_open_config'] = self.entrance_open_config
        if self.entrance_open_type:
            if hasattr(self.entrance_open_type, 'to_alipay_dict'):
                params['entrance_open_type'] = self.entrance_open_type.to_alipay_dict()
            else:
                params['entrance_open_type'] = self.entrance_open_type
        if self.need_owner_check:
            if hasattr(self.need_owner_check, 'to_alipay_dict'):
                params['need_owner_check'] = self.need_owner_check.to_alipay_dict()
            else:
                params['need_owner_check'] = self.need_owner_check
        if self.owner_check_config:
            if hasattr(self.owner_check_config, 'to_alipay_dict'):
                params['owner_check_config'] = self.owner_check_config.to_alipay_dict()
            else:
                params['owner_check_config'] = self.owner_check_config
        if self.owner_check_type:
            if hasattr(self.owner_check_type, 'to_alipay_dict'):
                params['owner_check_type'] = self.owner_check_type.to_alipay_dict()
            else:
                params['owner_check_type'] = self.owner_check_type
        if self.support_open:
            if hasattr(self.support_open, 'to_alipay_dict'):
                params['support_open'] = self.support_open.to_alipay_dict()
            else:
                params['support_open'] = self.support_open
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VisitorConfigVO()
        if 'entrance_open_config' in d:
            o.entrance_open_config = d['entrance_open_config']
        if 'entrance_open_type' in d:
            o.entrance_open_type = d['entrance_open_type']
        if 'need_owner_check' in d:
            o.need_owner_check = d['need_owner_check']
        if 'owner_check_config' in d:
            o.owner_check_config = d['owner_check_config']
        if 'owner_check_type' in d:
            o.owner_check_type = d['owner_check_type']
        if 'support_open' in d:
            o.support_open = d['support_open']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


