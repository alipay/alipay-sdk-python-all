#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NfcPointRefreshEventTracking import NfcPointRefreshEventTracking
from alipay.aop.api.domain.NfcPointRefreshExposureRule import NfcPointRefreshExposureRule
from alipay.aop.api.domain.NfcPointRefreshMatchText import NfcPointRefreshMatchText
from alipay.aop.api.domain.NfcPointRefreshProcessSetting import NfcPointRefreshProcessSetting
from alipay.aop.api.domain.NfcPointRefreshResource import NfcPointRefreshResource
from alipay.aop.api.domain.NfcPointRefreshShowText import NfcPointRefreshShowText
from alipay.aop.api.domain.NfcPointRefreshVoiceResource import NfcPointRefreshVoiceResource


class NfcPointRefreshData(object):

    def __init__(self):
        self._atmosphere = None
        self._consume_value = None
        self._event_tracking_module = None
        self._exposure_rule = None
        self._item_type = None
        self._match_text = None
        self._message = None
        self._point_code = None
        self._process_setting = None
        self._process_value = None
        self._resources = None
        self._show_text = None
        self._voice_resources = None

    @property
    def atmosphere(self):
        return self._atmosphere

    @atmosphere.setter
    def atmosphere(self, value):
        self._atmosphere = value
    @property
    def consume_value(self):
        return self._consume_value

    @consume_value.setter
    def consume_value(self, value):
        self._consume_value = value
    @property
    def event_tracking_module(self):
        return self._event_tracking_module

    @event_tracking_module.setter
    def event_tracking_module(self, value):
        if isinstance(value, NfcPointRefreshEventTracking):
            self._event_tracking_module = value
        else:
            self._event_tracking_module = NfcPointRefreshEventTracking.from_alipay_dict(value)
    @property
    def exposure_rule(self):
        return self._exposure_rule

    @exposure_rule.setter
    def exposure_rule(self, value):
        if isinstance(value, NfcPointRefreshExposureRule):
            self._exposure_rule = value
        else:
            self._exposure_rule = NfcPointRefreshExposureRule.from_alipay_dict(value)
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def match_text(self):
        return self._match_text

    @match_text.setter
    def match_text(self, value):
        if isinstance(value, NfcPointRefreshMatchText):
            self._match_text = value
        else:
            self._match_text = NfcPointRefreshMatchText.from_alipay_dict(value)
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def point_code(self):
        return self._point_code

    @point_code.setter
    def point_code(self, value):
        self._point_code = value
    @property
    def process_setting(self):
        return self._process_setting

    @process_setting.setter
    def process_setting(self, value):
        if isinstance(value, NfcPointRefreshProcessSetting):
            self._process_setting = value
        else:
            self._process_setting = NfcPointRefreshProcessSetting.from_alipay_dict(value)
    @property
    def process_value(self):
        return self._process_value

    @process_value.setter
    def process_value(self, value):
        self._process_value = value
    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        if isinstance(value, list):
            self._resources = list()
            for i in value:
                if isinstance(i, NfcPointRefreshResource):
                    self._resources.append(i)
                else:
                    self._resources.append(NfcPointRefreshResource.from_alipay_dict(i))
    @property
    def show_text(self):
        return self._show_text

    @show_text.setter
    def show_text(self, value):
        if isinstance(value, NfcPointRefreshShowText):
            self._show_text = value
        else:
            self._show_text = NfcPointRefreshShowText.from_alipay_dict(value)
    @property
    def voice_resources(self):
        return self._voice_resources

    @voice_resources.setter
    def voice_resources(self, value):
        if isinstance(value, list):
            self._voice_resources = list()
            for i in value:
                if isinstance(i, NfcPointRefreshVoiceResource):
                    self._voice_resources.append(i)
                else:
                    self._voice_resources.append(NfcPointRefreshVoiceResource.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.atmosphere:
            if hasattr(self.atmosphere, 'to_alipay_dict'):
                params['atmosphere'] = self.atmosphere.to_alipay_dict()
            else:
                params['atmosphere'] = self.atmosphere
        if self.consume_value:
            if hasattr(self.consume_value, 'to_alipay_dict'):
                params['consume_value'] = self.consume_value.to_alipay_dict()
            else:
                params['consume_value'] = self.consume_value
        if self.event_tracking_module:
            if hasattr(self.event_tracking_module, 'to_alipay_dict'):
                params['event_tracking_module'] = self.event_tracking_module.to_alipay_dict()
            else:
                params['event_tracking_module'] = self.event_tracking_module
        if self.exposure_rule:
            if hasattr(self.exposure_rule, 'to_alipay_dict'):
                params['exposure_rule'] = self.exposure_rule.to_alipay_dict()
            else:
                params['exposure_rule'] = self.exposure_rule
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.match_text:
            if hasattr(self.match_text, 'to_alipay_dict'):
                params['match_text'] = self.match_text.to_alipay_dict()
            else:
                params['match_text'] = self.match_text
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.point_code:
            if hasattr(self.point_code, 'to_alipay_dict'):
                params['point_code'] = self.point_code.to_alipay_dict()
            else:
                params['point_code'] = self.point_code
        if self.process_setting:
            if hasattr(self.process_setting, 'to_alipay_dict'):
                params['process_setting'] = self.process_setting.to_alipay_dict()
            else:
                params['process_setting'] = self.process_setting
        if self.process_value:
            if hasattr(self.process_value, 'to_alipay_dict'):
                params['process_value'] = self.process_value.to_alipay_dict()
            else:
                params['process_value'] = self.process_value
        if self.resources:
            if isinstance(self.resources, list):
                for i in range(0, len(self.resources)):
                    element = self.resources[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resources[i] = element.to_alipay_dict()
            if hasattr(self.resources, 'to_alipay_dict'):
                params['resources'] = self.resources.to_alipay_dict()
            else:
                params['resources'] = self.resources
        if self.show_text:
            if hasattr(self.show_text, 'to_alipay_dict'):
                params['show_text'] = self.show_text.to_alipay_dict()
            else:
                params['show_text'] = self.show_text
        if self.voice_resources:
            if isinstance(self.voice_resources, list):
                for i in range(0, len(self.voice_resources)):
                    element = self.voice_resources[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voice_resources[i] = element.to_alipay_dict()
            if hasattr(self.voice_resources, 'to_alipay_dict'):
                params['voice_resources'] = self.voice_resources.to_alipay_dict()
            else:
                params['voice_resources'] = self.voice_resources
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshData()
        if 'atmosphere' in d:
            o.atmosphere = d['atmosphere']
        if 'consume_value' in d:
            o.consume_value = d['consume_value']
        if 'event_tracking_module' in d:
            o.event_tracking_module = d['event_tracking_module']
        if 'exposure_rule' in d:
            o.exposure_rule = d['exposure_rule']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'match_text' in d:
            o.match_text = d['match_text']
        if 'message' in d:
            o.message = d['message']
        if 'point_code' in d:
            o.point_code = d['point_code']
        if 'process_setting' in d:
            o.process_setting = d['process_setting']
        if 'process_value' in d:
            o.process_value = d['process_value']
        if 'resources' in d:
            o.resources = d['resources']
        if 'show_text' in d:
            o.show_text = d['show_text']
        if 'voice_resources' in d:
            o.voice_resources = d['voice_resources']
        return o


