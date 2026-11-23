#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorAgentInfo(object):

    def __init__(self):
        self._agent_id = None
        self._agent_img = None
        self._agent_url = None
        self._arec_agent_id = None
        self._avatar_id = None
        self._department_name = None
        self._doctor_id = None
        self._doctor_name = None
        self._enabled = None
        self._enabled_home = None
        self._hospital_accreditation = None
        self._hospital_name = None
        self._popular_assistant_flag = None
        self._released_config_id = None
        self._title = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_img(self):
        return self._agent_img

    @agent_img.setter
    def agent_img(self, value):
        self._agent_img = value
    @property
    def agent_url(self):
        return self._agent_url

    @agent_url.setter
    def agent_url(self, value):
        self._agent_url = value
    @property
    def arec_agent_id(self):
        return self._arec_agent_id

    @arec_agent_id.setter
    def arec_agent_id(self, value):
        self._arec_agent_id = value
    @property
    def avatar_id(self):
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, value):
        self._avatar_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value
    @property
    def enabled_home(self):
        return self._enabled_home

    @enabled_home.setter
    def enabled_home(self, value):
        self._enabled_home = value
    @property
    def hospital_accreditation(self):
        return self._hospital_accreditation

    @hospital_accreditation.setter
    def hospital_accreditation(self, value):
        self._hospital_accreditation = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def popular_assistant_flag(self):
        return self._popular_assistant_flag

    @popular_assistant_flag.setter
    def popular_assistant_flag(self, value):
        self._popular_assistant_flag = value
    @property
    def released_config_id(self):
        return self._released_config_id

    @released_config_id.setter
    def released_config_id(self, value):
        self._released_config_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agent_img:
            if hasattr(self.agent_img, 'to_alipay_dict'):
                params['agent_img'] = self.agent_img.to_alipay_dict()
            else:
                params['agent_img'] = self.agent_img
        if self.agent_url:
            if hasattr(self.agent_url, 'to_alipay_dict'):
                params['agent_url'] = self.agent_url.to_alipay_dict()
            else:
                params['agent_url'] = self.agent_url
        if self.arec_agent_id:
            if hasattr(self.arec_agent_id, 'to_alipay_dict'):
                params['arec_agent_id'] = self.arec_agent_id.to_alipay_dict()
            else:
                params['arec_agent_id'] = self.arec_agent_id
        if self.avatar_id:
            if hasattr(self.avatar_id, 'to_alipay_dict'):
                params['avatar_id'] = self.avatar_id.to_alipay_dict()
            else:
                params['avatar_id'] = self.avatar_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.enabled:
            if hasattr(self.enabled, 'to_alipay_dict'):
                params['enabled'] = self.enabled.to_alipay_dict()
            else:
                params['enabled'] = self.enabled
        if self.enabled_home:
            if hasattr(self.enabled_home, 'to_alipay_dict'):
                params['enabled_home'] = self.enabled_home.to_alipay_dict()
            else:
                params['enabled_home'] = self.enabled_home
        if self.hospital_accreditation:
            if hasattr(self.hospital_accreditation, 'to_alipay_dict'):
                params['hospital_accreditation'] = self.hospital_accreditation.to_alipay_dict()
            else:
                params['hospital_accreditation'] = self.hospital_accreditation
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.popular_assistant_flag:
            if hasattr(self.popular_assistant_flag, 'to_alipay_dict'):
                params['popular_assistant_flag'] = self.popular_assistant_flag.to_alipay_dict()
            else:
                params['popular_assistant_flag'] = self.popular_assistant_flag
        if self.released_config_id:
            if hasattr(self.released_config_id, 'to_alipay_dict'):
                params['released_config_id'] = self.released_config_id.to_alipay_dict()
            else:
                params['released_config_id'] = self.released_config_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorAgentInfo()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agent_img' in d:
            o.agent_img = d['agent_img']
        if 'agent_url' in d:
            o.agent_url = d['agent_url']
        if 'arec_agent_id' in d:
            o.arec_agent_id = d['arec_agent_id']
        if 'avatar_id' in d:
            o.avatar_id = d['avatar_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'enabled' in d:
            o.enabled = d['enabled']
        if 'enabled_home' in d:
            o.enabled_home = d['enabled_home']
        if 'hospital_accreditation' in d:
            o.hospital_accreditation = d['hospital_accreditation']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'popular_assistant_flag' in d:
            o.popular_assistant_flag = d['popular_assistant_flag']
        if 'released_config_id' in d:
            o.released_config_id = d['released_config_id']
        if 'title' in d:
            o.title = d['title']
        return o


