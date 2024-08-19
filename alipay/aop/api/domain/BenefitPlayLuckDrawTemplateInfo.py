#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitTemplateDisplayInfo import BenefitTemplateDisplayInfo
from alipay.aop.api.domain.BenefitRewardInfo import BenefitRewardInfo


class BenefitPlayLuckDrawTemplateInfo(object):

    def __init__(self):
        self._code = None
        self._display_info = None
        self._end_time = None
        self._priority = None
        self._reward_info = None
        self._scene_code = None
        self._start_time = None
        self._status = None
        self._sub_scene_code = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        if isinstance(value, BenefitTemplateDisplayInfo):
            self._display_info = value
        else:
            self._display_info = BenefitTemplateDisplayInfo.from_alipay_dict(value)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def reward_info(self):
        return self._reward_info

    @reward_info.setter
    def reward_info(self, value):
        if isinstance(value, BenefitRewardInfo):
            self._reward_info = value
        else:
            self._reward_info = BenefitRewardInfo.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_scene_code(self):
        return self._sub_scene_code

    @sub_scene_code.setter
    def sub_scene_code(self, value):
        self._sub_scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.display_info:
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.reward_info:
            if hasattr(self.reward_info, 'to_alipay_dict'):
                params['reward_info'] = self.reward_info.to_alipay_dict()
            else:
                params['reward_info'] = self.reward_info
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_scene_code:
            if hasattr(self.sub_scene_code, 'to_alipay_dict'):
                params['sub_scene_code'] = self.sub_scene_code.to_alipay_dict()
            else:
                params['sub_scene_code'] = self.sub_scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitPlayLuckDrawTemplateInfo()
        if 'code' in d:
            o.code = d['code']
        if 'display_info' in d:
            o.display_info = d['display_info']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'priority' in d:
            o.priority = d['priority']
        if 'reward_info' in d:
            o.reward_info = d['reward_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_scene_code' in d:
            o.sub_scene_code = d['sub_scene_code']
        return o


