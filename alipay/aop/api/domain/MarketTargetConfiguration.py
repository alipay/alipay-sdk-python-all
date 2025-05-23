#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketTargetConfigurationActionProperty import MarketTargetConfigurationActionProperty


class MarketTargetConfiguration(object):

    def __init__(self):
        self._action_property_list = None

    @property
    def action_property_list(self):
        return self._action_property_list

    @action_property_list.setter
    def action_property_list(self, value):
        if isinstance(value, list):
            self._action_property_list = list()
            for i in value:
                if isinstance(i, MarketTargetConfigurationActionProperty):
                    self._action_property_list.append(i)
                else:
                    self._action_property_list.append(MarketTargetConfigurationActionProperty.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action_property_list:
            if isinstance(self.action_property_list, list):
                for i in range(0, len(self.action_property_list)):
                    element = self.action_property_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.action_property_list[i] = element.to_alipay_dict()
            if hasattr(self.action_property_list, 'to_alipay_dict'):
                params['action_property_list'] = self.action_property_list.to_alipay_dict()
            else:
                params['action_property_list'] = self.action_property_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketTargetConfiguration()
        if 'action_property_list' in d:
            o.action_property_list = d['action_property_list']
        return o


