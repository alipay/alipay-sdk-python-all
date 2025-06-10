#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduPeriodConfig import EduPeriodConfig


class EduPeriodInfo(object):

    def __init__(self):
        self._inst_id = None
        self._period_config_list = None
        self._period_desc = None
        self._period_id = None
        self._period_name = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def period_config_list(self):
        return self._period_config_list

    @period_config_list.setter
    def period_config_list(self, value):
        if isinstance(value, list):
            self._period_config_list = list()
            for i in value:
                if isinstance(i, EduPeriodConfig):
                    self._period_config_list.append(i)
                else:
                    self._period_config_list.append(EduPeriodConfig.from_alipay_dict(i))
    @property
    def period_desc(self):
        return self._period_desc

    @period_desc.setter
    def period_desc(self, value):
        self._period_desc = value
    @property
    def period_id(self):
        return self._period_id

    @period_id.setter
    def period_id(self, value):
        self._period_id = value
    @property
    def period_name(self):
        return self._period_name

    @period_name.setter
    def period_name(self, value):
        self._period_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.period_config_list:
            if isinstance(self.period_config_list, list):
                for i in range(0, len(self.period_config_list)):
                    element = self.period_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_config_list[i] = element.to_alipay_dict()
            if hasattr(self.period_config_list, 'to_alipay_dict'):
                params['period_config_list'] = self.period_config_list.to_alipay_dict()
            else:
                params['period_config_list'] = self.period_config_list
        if self.period_desc:
            if hasattr(self.period_desc, 'to_alipay_dict'):
                params['period_desc'] = self.period_desc.to_alipay_dict()
            else:
                params['period_desc'] = self.period_desc
        if self.period_id:
            if hasattr(self.period_id, 'to_alipay_dict'):
                params['period_id'] = self.period_id.to_alipay_dict()
            else:
                params['period_id'] = self.period_id
        if self.period_name:
            if hasattr(self.period_name, 'to_alipay_dict'):
                params['period_name'] = self.period_name.to_alipay_dict()
            else:
                params['period_name'] = self.period_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduPeriodInfo()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'period_config_list' in d:
            o.period_config_list = d['period_config_list']
        if 'period_desc' in d:
            o.period_desc = d['period_desc']
        if 'period_id' in d:
            o.period_id = d['period_id']
        if 'period_name' in d:
            o.period_name = d['period_name']
        return o


