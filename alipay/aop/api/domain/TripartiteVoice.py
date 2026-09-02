#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TripartiteVoice(object):

    def __init__(self):
        self._anteye_intention_l_1 = None
        self._anteye_intention_l_2 = None
        self._anteye_intention_l_3 = None
        self._app_version = None
        self._bus_date = None
        self._city = None
        self._content = None
        self._content_abstract = None
        self._gmt_create = None
        self._handle_time = None
        self._online_mode = None
        self._phone_system = None
        self._problem_type = None
        self._process_status = None
        self._province = None
        self._reason = None
        self._source_url = None
        self._title = None
        self._user_id = None
        self._voice_channel = None
        self._voice_id = None

    @property
    def anteye_intention_l_1(self):
        return self._anteye_intention_l_1

    @anteye_intention_l_1.setter
    def anteye_intention_l_1(self, value):
        self._anteye_intention_l_1 = value
    @property
    def anteye_intention_l_2(self):
        return self._anteye_intention_l_2

    @anteye_intention_l_2.setter
    def anteye_intention_l_2(self, value):
        self._anteye_intention_l_2 = value
    @property
    def anteye_intention_l_3(self):
        return self._anteye_intention_l_3

    @anteye_intention_l_3.setter
    def anteye_intention_l_3(self, value):
        self._anteye_intention_l_3 = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bus_date(self):
        return self._bus_date

    @bus_date.setter
    def bus_date(self, value):
        self._bus_date = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_abstract(self):
        return self._content_abstract

    @content_abstract.setter
    def content_abstract(self, value):
        self._content_abstract = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def handle_time(self):
        return self._handle_time

    @handle_time.setter
    def handle_time(self, value):
        self._handle_time = value
    @property
    def online_mode(self):
        return self._online_mode

    @online_mode.setter
    def online_mode(self, value):
        self._online_mode = value
    @property
    def phone_system(self):
        return self._phone_system

    @phone_system.setter
    def phone_system(self, value):
        self._phone_system = value
    @property
    def problem_type(self):
        return self._problem_type

    @problem_type.setter
    def problem_type(self, value):
        self._problem_type = value
    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, value):
        self._process_status = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        if isinstance(value, list):
            self._source_url = list()
            for i in value:
                self._source_url.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voice_channel(self):
        return self._voice_channel

    @voice_channel.setter
    def voice_channel(self, value):
        self._voice_channel = value
    @property
    def voice_id(self):
        return self._voice_id

    @voice_id.setter
    def voice_id(self, value):
        self._voice_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.anteye_intention_l_1:
            if hasattr(self.anteye_intention_l_1, 'to_alipay_dict'):
                params['anteye_intention_l_1'] = self.anteye_intention_l_1.to_alipay_dict()
            else:
                params['anteye_intention_l_1'] = self.anteye_intention_l_1
        if self.anteye_intention_l_2:
            if hasattr(self.anteye_intention_l_2, 'to_alipay_dict'):
                params['anteye_intention_l_2'] = self.anteye_intention_l_2.to_alipay_dict()
            else:
                params['anteye_intention_l_2'] = self.anteye_intention_l_2
        if self.anteye_intention_l_3:
            if hasattr(self.anteye_intention_l_3, 'to_alipay_dict'):
                params['anteye_intention_l_3'] = self.anteye_intention_l_3.to_alipay_dict()
            else:
                params['anteye_intention_l_3'] = self.anteye_intention_l_3
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.bus_date:
            if hasattr(self.bus_date, 'to_alipay_dict'):
                params['bus_date'] = self.bus_date.to_alipay_dict()
            else:
                params['bus_date'] = self.bus_date
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_abstract:
            if hasattr(self.content_abstract, 'to_alipay_dict'):
                params['content_abstract'] = self.content_abstract.to_alipay_dict()
            else:
                params['content_abstract'] = self.content_abstract
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.handle_time:
            if hasattr(self.handle_time, 'to_alipay_dict'):
                params['handle_time'] = self.handle_time.to_alipay_dict()
            else:
                params['handle_time'] = self.handle_time
        if self.online_mode:
            if hasattr(self.online_mode, 'to_alipay_dict'):
                params['online_mode'] = self.online_mode.to_alipay_dict()
            else:
                params['online_mode'] = self.online_mode
        if self.phone_system:
            if hasattr(self.phone_system, 'to_alipay_dict'):
                params['phone_system'] = self.phone_system.to_alipay_dict()
            else:
                params['phone_system'] = self.phone_system
        if self.problem_type:
            if hasattr(self.problem_type, 'to_alipay_dict'):
                params['problem_type'] = self.problem_type.to_alipay_dict()
            else:
                params['problem_type'] = self.problem_type
        if self.process_status:
            if hasattr(self.process_status, 'to_alipay_dict'):
                params['process_status'] = self.process_status.to_alipay_dict()
            else:
                params['process_status'] = self.process_status
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.source_url:
            if isinstance(self.source_url, list):
                for i in range(0, len(self.source_url)):
                    element = self.source_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_url[i] = element.to_alipay_dict()
            if hasattr(self.source_url, 'to_alipay_dict'):
                params['source_url'] = self.source_url.to_alipay_dict()
            else:
                params['source_url'] = self.source_url
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voice_channel:
            if hasattr(self.voice_channel, 'to_alipay_dict'):
                params['voice_channel'] = self.voice_channel.to_alipay_dict()
            else:
                params['voice_channel'] = self.voice_channel
        if self.voice_id:
            if hasattr(self.voice_id, 'to_alipay_dict'):
                params['voice_id'] = self.voice_id.to_alipay_dict()
            else:
                params['voice_id'] = self.voice_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TripartiteVoice()
        if 'anteye_intention_l_1' in d:
            o.anteye_intention_l_1 = d['anteye_intention_l_1']
        if 'anteye_intention_l_2' in d:
            o.anteye_intention_l_2 = d['anteye_intention_l_2']
        if 'anteye_intention_l_3' in d:
            o.anteye_intention_l_3 = d['anteye_intention_l_3']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bus_date' in d:
            o.bus_date = d['bus_date']
        if 'city' in d:
            o.city = d['city']
        if 'content' in d:
            o.content = d['content']
        if 'content_abstract' in d:
            o.content_abstract = d['content_abstract']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'handle_time' in d:
            o.handle_time = d['handle_time']
        if 'online_mode' in d:
            o.online_mode = d['online_mode']
        if 'phone_system' in d:
            o.phone_system = d['phone_system']
        if 'problem_type' in d:
            o.problem_type = d['problem_type']
        if 'process_status' in d:
            o.process_status = d['process_status']
        if 'province' in d:
            o.province = d['province']
        if 'reason' in d:
            o.reason = d['reason']
        if 'source_url' in d:
            o.source_url = d['source_url']
        if 'title' in d:
            o.title = d['title']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voice_channel' in d:
            o.voice_channel = d['voice_channel']
        if 'voice_id' in d:
            o.voice_id = d['voice_id']
        return o


