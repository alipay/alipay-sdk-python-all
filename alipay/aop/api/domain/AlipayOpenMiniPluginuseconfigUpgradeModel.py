#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniPluginuseconfigUpgradeModel(object):

    def __init__(self):
        self._bundle_id = None
        self._plugin_dev_version = None
        self._plugin_id = None
        self._strategy_value = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def plugin_dev_version(self):
        return self._plugin_dev_version

    @plugin_dev_version.setter
    def plugin_dev_version(self, value):
        self._plugin_dev_version = value
    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def strategy_value(self):
        return self._strategy_value

    @strategy_value.setter
    def strategy_value(self, value):
        self._strategy_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.plugin_dev_version:
            if hasattr(self.plugin_dev_version, 'to_alipay_dict'):
                params['plugin_dev_version'] = self.plugin_dev_version.to_alipay_dict()
            else:
                params['plugin_dev_version'] = self.plugin_dev_version
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.strategy_value:
            if hasattr(self.strategy_value, 'to_alipay_dict'):
                params['strategy_value'] = self.strategy_value.to_alipay_dict()
            else:
                params['strategy_value'] = self.strategy_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniPluginuseconfigUpgradeModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'plugin_dev_version' in d:
            o.plugin_dev_version = d['plugin_dev_version']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'strategy_value' in d:
            o.strategy_value = d['strategy_value']
        return o


