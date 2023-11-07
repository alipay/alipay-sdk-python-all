#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParamEntry import ParamEntry


class AlipayMerchantQipanCommoninsightQueryModel(object):

    def __init__(self):
        self._owner_pid = None
        self._param_list = None
        self._report_date = None
        self._scene_code = None

    @property
    def owner_pid(self):
        return self._owner_pid

    @owner_pid.setter
    def owner_pid(self, value):
        self._owner_pid = value
    @property
    def param_list(self):
        return self._param_list

    @param_list.setter
    def param_list(self, value):
        if isinstance(value, list):
            self._param_list = list()
            for i in value:
                if isinstance(i, ParamEntry):
                    self._param_list.append(i)
                else:
                    self._param_list.append(ParamEntry.from_alipay_dict(i))
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.owner_pid:
            if hasattr(self.owner_pid, 'to_alipay_dict'):
                params['owner_pid'] = self.owner_pid.to_alipay_dict()
            else:
                params['owner_pid'] = self.owner_pid
        if self.param_list:
            if isinstance(self.param_list, list):
                for i in range(0, len(self.param_list)):
                    element = self.param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.param_list[i] = element.to_alipay_dict()
            if hasattr(self.param_list, 'to_alipay_dict'):
                params['param_list'] = self.param_list.to_alipay_dict()
            else:
                params['param_list'] = self.param_list
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanCommoninsightQueryModel()
        if 'owner_pid' in d:
            o.owner_pid = d['owner_pid']
        if 'param_list' in d:
            o.param_list = d['param_list']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


