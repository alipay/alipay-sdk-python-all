#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnergyExtRequest import EnergyExtRequest
from alipay.aop.api.domain.GreenAction import GreenAction


class AlipaySocialOpengreenEnergySendModel(object):

    def __init__(self):
        self._action_time = None
        self._biz_no = None
        self._energy_app_id = None
        self._ext_info = None
        self._green_actions = None
        self._open_id = None
        self._pid = None
        self._source = None
        self._user_id = None

    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def energy_app_id(self):
        return self._energy_app_id

    @energy_app_id.setter
    def energy_app_id(self, value):
        self._energy_app_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, EnergyExtRequest):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(EnergyExtRequest.from_alipay_dict(i))
    @property
    def green_actions(self):
        return self._green_actions

    @green_actions.setter
    def green_actions(self, value):
        if isinstance(value, list):
            self._green_actions = list()
            for i in value:
                if isinstance(i, GreenAction):
                    self._green_actions.append(i)
                else:
                    self._green_actions.append(GreenAction.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.energy_app_id:
            if hasattr(self.energy_app_id, 'to_alipay_dict'):
                params['energy_app_id'] = self.energy_app_id.to_alipay_dict()
            else:
                params['energy_app_id'] = self.energy_app_id
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.green_actions:
            if isinstance(self.green_actions, list):
                for i in range(0, len(self.green_actions)):
                    element = self.green_actions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.green_actions[i] = element.to_alipay_dict()
            if hasattr(self.green_actions, 'to_alipay_dict'):
                params['green_actions'] = self.green_actions.to_alipay_dict()
            else:
                params['green_actions'] = self.green_actions
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialOpengreenEnergySendModel()
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'energy_app_id' in d:
            o.energy_app_id = d['energy_app_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'green_actions' in d:
            o.green_actions = d['green_actions']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


