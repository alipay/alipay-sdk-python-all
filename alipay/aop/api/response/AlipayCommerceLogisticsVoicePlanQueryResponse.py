#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsVoicePlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsVoicePlanQueryResponse, self).__init__()
        self._biz_date = None
        self._end_time = None
        self._logistics_voice_plan_id = None
        self._plan_name = None
        self._plan_status = None
        self._scene_type = None
        self._sn_fail_count = None
        self._sn_success_count = None
        self._sn_total_count = None
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
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def sn_fail_count(self):
        return self._sn_fail_count

    @sn_fail_count.setter
    def sn_fail_count(self, value):
        self._sn_fail_count = value
    @property
    def sn_success_count(self):
        return self._sn_success_count

    @sn_success_count.setter
    def sn_success_count(self, value):
        self._sn_success_count = value
    @property
    def sn_total_count(self):
        return self._sn_total_count

    @sn_total_count.setter
    def sn_total_count(self, value):
        self._sn_total_count = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsVoicePlanQueryResponse, self).parse_response_content(response_content)
        if 'biz_date' in response:
            self.biz_date = response['biz_date']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'logistics_voice_plan_id' in response:
            self.logistics_voice_plan_id = response['logistics_voice_plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'plan_status' in response:
            self.plan_status = response['plan_status']
        if 'scene_type' in response:
            self.scene_type = response['scene_type']
        if 'sn_fail_count' in response:
            self.sn_fail_count = response['sn_fail_count']
        if 'sn_success_count' in response:
            self.sn_success_count = response['sn_success_count']
        if 'sn_total_count' in response:
            self.sn_total_count = response['sn_total_count']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'voice_template_id' in response:
            self.voice_template_id = response['voice_template_id']
