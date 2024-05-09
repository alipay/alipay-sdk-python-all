#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlarmSubscribe import AlarmSubscribe


class AlipayCloudCloudbaseMonitorAlarmsubscribeModifyModel(object):

    def __init__(self):
        self._alarm_subscribes = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._rule_id = None

    @property
    def alarm_subscribes(self):
        return self._alarm_subscribes

    @alarm_subscribes.setter
    def alarm_subscribes(self, value):
        if isinstance(value, list):
            self._alarm_subscribes = list()
            for i in value:
                if isinstance(i, AlarmSubscribe):
                    self._alarm_subscribes.append(i)
                else:
                    self._alarm_subscribes.append(AlarmSubscribe.from_alipay_dict(i))
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_subscribes:
            if isinstance(self.alarm_subscribes, list):
                for i in range(0, len(self.alarm_subscribes)):
                    element = self.alarm_subscribes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alarm_subscribes[i] = element.to_alipay_dict()
            if hasattr(self.alarm_subscribes, 'to_alipay_dict'):
                params['alarm_subscribes'] = self.alarm_subscribes.to_alipay_dict()
            else:
                params['alarm_subscribes'] = self.alarm_subscribes
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseMonitorAlarmsubscribeModifyModel()
        if 'alarm_subscribes' in d:
            o.alarm_subscribes = d['alarm_subscribes']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        return o


