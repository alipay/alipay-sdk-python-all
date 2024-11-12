#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitActivity import BenefitActivity
from alipay.aop.api.domain.DisplaySetting import DisplaySetting
from alipay.aop.api.domain.PromoActActivity import PromoActActivity


class AlipayOpenMiniMiniappLayerCreateModel(object):

    def __init__(self):
        self._activity_name = None
        self._benefit_activity_list = None
        self._channel_code_list = None
        self._city_code_list = None
        self._display_setting = None
        self._end_time = None
        self._fatigue_count = None
        self._layer_show_time_begin = None
        self._layer_show_time_end = None
        self._mrch_crowd_list = None
        self._promo_activity_list = None
        self._start_time = None
        self._target = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def benefit_activity_list(self):
        return self._benefit_activity_list

    @benefit_activity_list.setter
    def benefit_activity_list(self, value):
        if isinstance(value, list):
            self._benefit_activity_list = list()
            for i in value:
                if isinstance(i, BenefitActivity):
                    self._benefit_activity_list.append(i)
                else:
                    self._benefit_activity_list.append(BenefitActivity.from_alipay_dict(i))
    @property
    def channel_code_list(self):
        return self._channel_code_list

    @channel_code_list.setter
    def channel_code_list(self, value):
        if isinstance(value, list):
            self._channel_code_list = list()
            for i in value:
                self._channel_code_list.append(i)
    @property
    def city_code_list(self):
        return self._city_code_list

    @city_code_list.setter
    def city_code_list(self, value):
        if isinstance(value, list):
            self._city_code_list = list()
            for i in value:
                self._city_code_list.append(i)
    @property
    def display_setting(self):
        return self._display_setting

    @display_setting.setter
    def display_setting(self, value):
        if isinstance(value, DisplaySetting):
            self._display_setting = value
        else:
            self._display_setting = DisplaySetting.from_alipay_dict(value)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fatigue_count(self):
        return self._fatigue_count

    @fatigue_count.setter
    def fatigue_count(self, value):
        self._fatigue_count = value
    @property
    def layer_show_time_begin(self):
        return self._layer_show_time_begin

    @layer_show_time_begin.setter
    def layer_show_time_begin(self, value):
        self._layer_show_time_begin = value
    @property
    def layer_show_time_end(self):
        return self._layer_show_time_end

    @layer_show_time_end.setter
    def layer_show_time_end(self, value):
        self._layer_show_time_end = value
    @property
    def mrch_crowd_list(self):
        return self._mrch_crowd_list

    @mrch_crowd_list.setter
    def mrch_crowd_list(self, value):
        if isinstance(value, list):
            self._mrch_crowd_list = list()
            for i in value:
                self._mrch_crowd_list.append(i)
    @property
    def promo_activity_list(self):
        return self._promo_activity_list

    @promo_activity_list.setter
    def promo_activity_list(self, value):
        if isinstance(value, list):
            self._promo_activity_list = list()
            for i in value:
                if isinstance(i, PromoActActivity):
                    self._promo_activity_list.append(i)
                else:
                    self._promo_activity_list.append(PromoActActivity.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.benefit_activity_list:
            if isinstance(self.benefit_activity_list, list):
                for i in range(0, len(self.benefit_activity_list)):
                    element = self.benefit_activity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_activity_list[i] = element.to_alipay_dict()
            if hasattr(self.benefit_activity_list, 'to_alipay_dict'):
                params['benefit_activity_list'] = self.benefit_activity_list.to_alipay_dict()
            else:
                params['benefit_activity_list'] = self.benefit_activity_list
        if self.channel_code_list:
            if isinstance(self.channel_code_list, list):
                for i in range(0, len(self.channel_code_list)):
                    element = self.channel_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_code_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_code_list, 'to_alipay_dict'):
                params['channel_code_list'] = self.channel_code_list.to_alipay_dict()
            else:
                params['channel_code_list'] = self.channel_code_list
        if self.city_code_list:
            if isinstance(self.city_code_list, list):
                for i in range(0, len(self.city_code_list)):
                    element = self.city_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_code_list[i] = element.to_alipay_dict()
            if hasattr(self.city_code_list, 'to_alipay_dict'):
                params['city_code_list'] = self.city_code_list.to_alipay_dict()
            else:
                params['city_code_list'] = self.city_code_list
        if self.display_setting:
            if hasattr(self.display_setting, 'to_alipay_dict'):
                params['display_setting'] = self.display_setting.to_alipay_dict()
            else:
                params['display_setting'] = self.display_setting
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fatigue_count:
            if hasattr(self.fatigue_count, 'to_alipay_dict'):
                params['fatigue_count'] = self.fatigue_count.to_alipay_dict()
            else:
                params['fatigue_count'] = self.fatigue_count
        if self.layer_show_time_begin:
            if hasattr(self.layer_show_time_begin, 'to_alipay_dict'):
                params['layer_show_time_begin'] = self.layer_show_time_begin.to_alipay_dict()
            else:
                params['layer_show_time_begin'] = self.layer_show_time_begin
        if self.layer_show_time_end:
            if hasattr(self.layer_show_time_end, 'to_alipay_dict'):
                params['layer_show_time_end'] = self.layer_show_time_end.to_alipay_dict()
            else:
                params['layer_show_time_end'] = self.layer_show_time_end
        if self.mrch_crowd_list:
            if isinstance(self.mrch_crowd_list, list):
                for i in range(0, len(self.mrch_crowd_list)):
                    element = self.mrch_crowd_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mrch_crowd_list[i] = element.to_alipay_dict()
            if hasattr(self.mrch_crowd_list, 'to_alipay_dict'):
                params['mrch_crowd_list'] = self.mrch_crowd_list.to_alipay_dict()
            else:
                params['mrch_crowd_list'] = self.mrch_crowd_list
        if self.promo_activity_list:
            if isinstance(self.promo_activity_list, list):
                for i in range(0, len(self.promo_activity_list)):
                    element = self.promo_activity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_activity_list[i] = element.to_alipay_dict()
            if hasattr(self.promo_activity_list, 'to_alipay_dict'):
                params['promo_activity_list'] = self.promo_activity_list.to_alipay_dict()
            else:
                params['promo_activity_list'] = self.promo_activity_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMiniappLayerCreateModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'benefit_activity_list' in d:
            o.benefit_activity_list = d['benefit_activity_list']
        if 'channel_code_list' in d:
            o.channel_code_list = d['channel_code_list']
        if 'city_code_list' in d:
            o.city_code_list = d['city_code_list']
        if 'display_setting' in d:
            o.display_setting = d['display_setting']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fatigue_count' in d:
            o.fatigue_count = d['fatigue_count']
        if 'layer_show_time_begin' in d:
            o.layer_show_time_begin = d['layer_show_time_begin']
        if 'layer_show_time_end' in d:
            o.layer_show_time_end = d['layer_show_time_end']
        if 'mrch_crowd_list' in d:
            o.mrch_crowd_list = d['mrch_crowd_list']
        if 'promo_activity_list' in d:
            o.promo_activity_list = d['promo_activity_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'target' in d:
            o.target = d['target']
        return o


