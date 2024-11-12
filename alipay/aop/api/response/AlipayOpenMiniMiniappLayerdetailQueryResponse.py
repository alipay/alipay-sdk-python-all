#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitActivity import BenefitActivity
from alipay.aop.api.domain.ChannelCodeInfo import ChannelCodeInfo
from alipay.aop.api.domain.DisplaySetting import DisplaySetting
from alipay.aop.api.domain.PromoActActivity import PromoActActivity


class AlipayOpenMiniMiniappLayerdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappLayerdetailQueryResponse, self).__init__()
        self._activity_id = None
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
        self._status = None
        self._target = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
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
                if isinstance(i, ChannelCodeInfo):
                    self._channel_code_list.append(i)
                else:
                    self._channel_code_list.append(ChannelCodeInfo.from_alipay_dict(i))
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappLayerdetailQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'benefit_activity_list' in response:
            self.benefit_activity_list = response['benefit_activity_list']
        if 'channel_code_list' in response:
            self.channel_code_list = response['channel_code_list']
        if 'city_code_list' in response:
            self.city_code_list = response['city_code_list']
        if 'display_setting' in response:
            self.display_setting = response['display_setting']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'fatigue_count' in response:
            self.fatigue_count = response['fatigue_count']
        if 'layer_show_time_begin' in response:
            self.layer_show_time_begin = response['layer_show_time_begin']
        if 'layer_show_time_end' in response:
            self.layer_show_time_end = response['layer_show_time_end']
        if 'mrch_crowd_list' in response:
            self.mrch_crowd_list = response['mrch_crowd_list']
        if 'promo_activity_list' in response:
            self.promo_activity_list = response['promo_activity_list']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'target' in response:
            self.target = response['target']
