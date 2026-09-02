#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsVoicePlanSaveModel(object):

    def __init__(self):
        self._biz_date = None
        self._end_time = None
        self._logistics_voice_plan_id = None
        self._plan_name = None
        self._scene_type = None
        self._sn_file_id = None
        self._start_time = None
        self._voice_template_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def logistics_voice_plan_id(self):
        return self._logistics_voice_plan_id

    @logistics_voice_plan_id.setter
    def logistics_voice_plan_id(self, value):
        self._logistics_voice_plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def sn_file_id(self):
        return self._sn_file_id

    @sn_file_id.setter
    def sn_file_id(self, value):
        self._sn_file_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def voice_template_id(self):
        return self._voice_template_id

    @voice_template_id.setter
    def voice_template_id(self, value):
        self._voice_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.logistics_voice_plan_id:
            if hasattr(self.logistics_voice_plan_id, 'to_alipay_dict'):
                params['logistics_voice_plan_id'] = self.logistics_voice_plan_id.to_alipay_dict()
            else:
                params['logistics_voice_plan_id'] = self.logistics_voice_plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.sn_file_id:
            if hasattr(self.sn_file_id, 'to_alipay_dict'):
                params['sn_file_id'] = self.sn_file_id.to_alipay_dict()
            else:
                params['sn_file_id'] = self.sn_file_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.voice_template_id:
            if hasattr(self.voice_template_id, 'to_alipay_dict'):
                params['voice_template_id'] = self.voice_template_id.to_alipay_dict()
            else:
                params['voice_template_id'] = self.voice_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsVoicePlanSaveModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'logistics_voice_plan_id' in d:
            o.logistics_voice_plan_id = d['logistics_voice_plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'sn_file_id' in d:
            o.sn_file_id = d['sn_file_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'voice_template_id' in d:
            o.voice_template_id = d['voice_template_id']
        return o


