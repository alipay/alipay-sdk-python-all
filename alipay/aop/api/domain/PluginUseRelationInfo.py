#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PluginUseConfigInfo import PluginUseConfigInfo


class PluginUseRelationInfo(object):

    def __init__(self):
        self._beta_memo = None
        self._beta_plugin_version = None
        self._beta_qr_code_url = None
        self._beta_status = None
        self._gmt_active = None
        self._gmt_create = None
        self._gmt_invalid = None
        self._mini_app_id = None
        self._plugin_deploy_version = None
        self._plugin_id = None
        self._plugin_status = None
        self._plugin_use_config_info_list = None
        self._plugin_version = None
        self._run_mode_type = None
        self._source_from = None

    @property
    def beta_memo(self):
        return self._beta_memo

    @beta_memo.setter
    def beta_memo(self, value):
        self._beta_memo = value
    @property
    def beta_plugin_version(self):
        return self._beta_plugin_version

    @beta_plugin_version.setter
    def beta_plugin_version(self, value):
        self._beta_plugin_version = value
    @property
    def beta_qr_code_url(self):
        return self._beta_qr_code_url

    @beta_qr_code_url.setter
    def beta_qr_code_url(self, value):
        self._beta_qr_code_url = value
    @property
    def beta_status(self):
        return self._beta_status

    @beta_status.setter
    def beta_status(self, value):
        self._beta_status = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_invalid(self):
        return self._gmt_invalid

    @gmt_invalid.setter
    def gmt_invalid(self, value):
        self._gmt_invalid = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def plugin_deploy_version(self):
        return self._plugin_deploy_version

    @plugin_deploy_version.setter
    def plugin_deploy_version(self, value):
        self._plugin_deploy_version = value
    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def plugin_status(self):
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, value):
        self._plugin_status = value
    @property
    def plugin_use_config_info_list(self):
        return self._plugin_use_config_info_list

    @plugin_use_config_info_list.setter
    def plugin_use_config_info_list(self, value):
        if isinstance(value, list):
            self._plugin_use_config_info_list = list()
            for i in value:
                if isinstance(i, PluginUseConfigInfo):
                    self._plugin_use_config_info_list.append(i)
                else:
                    self._plugin_use_config_info_list.append(PluginUseConfigInfo.from_alipay_dict(i))
    @property
    def plugin_version(self):
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, value):
        self._plugin_version = value
    @property
    def run_mode_type(self):
        return self._run_mode_type

    @run_mode_type.setter
    def run_mode_type(self, value):
        self._run_mode_type = value
    @property
    def source_from(self):
        return self._source_from

    @source_from.setter
    def source_from(self, value):
        self._source_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.beta_memo:
            if hasattr(self.beta_memo, 'to_alipay_dict'):
                params['beta_memo'] = self.beta_memo.to_alipay_dict()
            else:
                params['beta_memo'] = self.beta_memo
        if self.beta_plugin_version:
            if hasattr(self.beta_plugin_version, 'to_alipay_dict'):
                params['beta_plugin_version'] = self.beta_plugin_version.to_alipay_dict()
            else:
                params['beta_plugin_version'] = self.beta_plugin_version
        if self.beta_qr_code_url:
            if hasattr(self.beta_qr_code_url, 'to_alipay_dict'):
                params['beta_qr_code_url'] = self.beta_qr_code_url.to_alipay_dict()
            else:
                params['beta_qr_code_url'] = self.beta_qr_code_url
        if self.beta_status:
            if hasattr(self.beta_status, 'to_alipay_dict'):
                params['beta_status'] = self.beta_status.to_alipay_dict()
            else:
                params['beta_status'] = self.beta_status
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_invalid:
            if hasattr(self.gmt_invalid, 'to_alipay_dict'):
                params['gmt_invalid'] = self.gmt_invalid.to_alipay_dict()
            else:
                params['gmt_invalid'] = self.gmt_invalid
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.plugin_deploy_version:
            if hasattr(self.plugin_deploy_version, 'to_alipay_dict'):
                params['plugin_deploy_version'] = self.plugin_deploy_version.to_alipay_dict()
            else:
                params['plugin_deploy_version'] = self.plugin_deploy_version
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.plugin_status:
            if hasattr(self.plugin_status, 'to_alipay_dict'):
                params['plugin_status'] = self.plugin_status.to_alipay_dict()
            else:
                params['plugin_status'] = self.plugin_status
        if self.plugin_use_config_info_list:
            if isinstance(self.plugin_use_config_info_list, list):
                for i in range(0, len(self.plugin_use_config_info_list)):
                    element = self.plugin_use_config_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plugin_use_config_info_list[i] = element.to_alipay_dict()
            if hasattr(self.plugin_use_config_info_list, 'to_alipay_dict'):
                params['plugin_use_config_info_list'] = self.plugin_use_config_info_list.to_alipay_dict()
            else:
                params['plugin_use_config_info_list'] = self.plugin_use_config_info_list
        if self.plugin_version:
            if hasattr(self.plugin_version, 'to_alipay_dict'):
                params['plugin_version'] = self.plugin_version.to_alipay_dict()
            else:
                params['plugin_version'] = self.plugin_version
        if self.run_mode_type:
            if hasattr(self.run_mode_type, 'to_alipay_dict'):
                params['run_mode_type'] = self.run_mode_type.to_alipay_dict()
            else:
                params['run_mode_type'] = self.run_mode_type
        if self.source_from:
            if hasattr(self.source_from, 'to_alipay_dict'):
                params['source_from'] = self.source_from.to_alipay_dict()
            else:
                params['source_from'] = self.source_from
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PluginUseRelationInfo()
        if 'beta_memo' in d:
            o.beta_memo = d['beta_memo']
        if 'beta_plugin_version' in d:
            o.beta_plugin_version = d['beta_plugin_version']
        if 'beta_qr_code_url' in d:
            o.beta_qr_code_url = d['beta_qr_code_url']
        if 'beta_status' in d:
            o.beta_status = d['beta_status']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_invalid' in d:
            o.gmt_invalid = d['gmt_invalid']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'plugin_deploy_version' in d:
            o.plugin_deploy_version = d['plugin_deploy_version']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'plugin_status' in d:
            o.plugin_status = d['plugin_status']
        if 'plugin_use_config_info_list' in d:
            o.plugin_use_config_info_list = d['plugin_use_config_info_list']
        if 'plugin_version' in d:
            o.plugin_version = d['plugin_version']
        if 'run_mode_type' in d:
            o.run_mode_type = d['run_mode_type']
        if 'source_from' in d:
            o.source_from = d['source_from']
        return o


