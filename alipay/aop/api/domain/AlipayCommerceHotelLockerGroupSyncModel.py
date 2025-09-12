#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BarLinkInfo import BarLinkInfo
from alipay.aop.api.domain.GroupConfigModelConfig import GroupConfigModelConfig


class AlipayCommerceHotelLockerGroupSyncModel(object):

    def __init__(self):
        self._alipay_pid = None
        self._app_logo = None
        self._bar_links = None
        self._config_model = None
        self._mini_app_id = None
        self._mini_app_name = None
        self._org_group_code = None
        self._org_group_name = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def bar_links(self):
        return self._bar_links

    @bar_links.setter
    def bar_links(self, value):
        if isinstance(value, list):
            self._bar_links = list()
            for i in value:
                if isinstance(i, BarLinkInfo):
                    self._bar_links.append(i)
                else:
                    self._bar_links.append(BarLinkInfo.from_alipay_dict(i))
    @property
    def config_model(self):
        return self._config_model

    @config_model.setter
    def config_model(self, value):
        if isinstance(value, GroupConfigModelConfig):
            self._config_model = value
        else:
            self._config_model = GroupConfigModelConfig.from_alipay_dict(value)
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value
    @property
    def org_group_code(self):
        return self._org_group_code

    @org_group_code.setter
    def org_group_code(self, value):
        self._org_group_code = value
    @property
    def org_group_name(self):
        return self._org_group_name

    @org_group_name.setter
    def org_group_name(self, value):
        self._org_group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.bar_links:
            if isinstance(self.bar_links, list):
                for i in range(0, len(self.bar_links)):
                    element = self.bar_links[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bar_links[i] = element.to_alipay_dict()
            if hasattr(self.bar_links, 'to_alipay_dict'):
                params['bar_links'] = self.bar_links.to_alipay_dict()
            else:
                params['bar_links'] = self.bar_links
        if self.config_model:
            if hasattr(self.config_model, 'to_alipay_dict'):
                params['config_model'] = self.config_model.to_alipay_dict()
            else:
                params['config_model'] = self.config_model
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        if self.org_group_code:
            if hasattr(self.org_group_code, 'to_alipay_dict'):
                params['org_group_code'] = self.org_group_code.to_alipay_dict()
            else:
                params['org_group_code'] = self.org_group_code
        if self.org_group_name:
            if hasattr(self.org_group_name, 'to_alipay_dict'):
                params['org_group_name'] = self.org_group_name.to_alipay_dict()
            else:
                params['org_group_name'] = self.org_group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelLockerGroupSyncModel()
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'bar_links' in d:
            o.bar_links = d['bar_links']
        if 'config_model' in d:
            o.config_model = d['config_model']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        if 'org_group_code' in d:
            o.org_group_code = d['org_group_code']
        if 'org_group_name' in d:
            o.org_group_name = d['org_group_name']
        return o


