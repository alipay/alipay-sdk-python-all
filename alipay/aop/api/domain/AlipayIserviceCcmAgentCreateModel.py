#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgentChatInfo import AgentChatInfo
from alipay.aop.api.domain.AgentHotlineInfo import AgentHotlineInfo
from alipay.aop.api.domain.RoleId import RoleId


class AlipayIserviceCcmAgentCreateModel(object):

    def __init__(self):
        self._answering_mode = None
        self._ccs_instance_ids = None
        self._chat_configs = None
        self._creator_id = None
        self._email = None
        self._external_user_id = None
        self._hotline_configs = None
        self._job_number = None
        self._mobile = None
        self._nick_name = None
        self._real_name = None
        self._role_ids = None
        self._user_channel = None

    @property
    def answering_mode(self):
        return self._answering_mode

    @answering_mode.setter
    def answering_mode(self, value):
        self._answering_mode = value
    @property
    def ccs_instance_ids(self):
        return self._ccs_instance_ids

    @ccs_instance_ids.setter
    def ccs_instance_ids(self, value):
        if isinstance(value, list):
            self._ccs_instance_ids = list()
            for i in value:
                self._ccs_instance_ids.append(i)
    @property
    def chat_configs(self):
        return self._chat_configs

    @chat_configs.setter
    def chat_configs(self, value):
        if isinstance(value, list):
            self._chat_configs = list()
            for i in value:
                if isinstance(i, AgentChatInfo):
                    self._chat_configs.append(i)
                else:
                    self._chat_configs.append(AgentChatInfo.from_alipay_dict(i))
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def hotline_configs(self):
        return self._hotline_configs

    @hotline_configs.setter
    def hotline_configs(self, value):
        if isinstance(value, list):
            self._hotline_configs = list()
            for i in value:
                if isinstance(i, AgentHotlineInfo):
                    self._hotline_configs.append(i)
                else:
                    self._hotline_configs.append(AgentHotlineInfo.from_alipay_dict(i))
    @property
    def job_number(self):
        return self._job_number

    @job_number.setter
    def job_number(self, value):
        self._job_number = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def role_ids(self):
        return self._role_ids

    @role_ids.setter
    def role_ids(self, value):
        if isinstance(value, list):
            self._role_ids = list()
            for i in value:
                if isinstance(i, RoleId):
                    self._role_ids.append(i)
                else:
                    self._role_ids.append(RoleId.from_alipay_dict(i))
    @property
    def user_channel(self):
        return self._user_channel

    @user_channel.setter
    def user_channel(self, value):
        self._user_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.answering_mode:
            if hasattr(self.answering_mode, 'to_alipay_dict'):
                params['answering_mode'] = self.answering_mode.to_alipay_dict()
            else:
                params['answering_mode'] = self.answering_mode
        if self.ccs_instance_ids:
            if isinstance(self.ccs_instance_ids, list):
                for i in range(0, len(self.ccs_instance_ids)):
                    element = self.ccs_instance_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ccs_instance_ids[i] = element.to_alipay_dict()
            if hasattr(self.ccs_instance_ids, 'to_alipay_dict'):
                params['ccs_instance_ids'] = self.ccs_instance_ids.to_alipay_dict()
            else:
                params['ccs_instance_ids'] = self.ccs_instance_ids
        if self.chat_configs:
            if isinstance(self.chat_configs, list):
                for i in range(0, len(self.chat_configs)):
                    element = self.chat_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_configs[i] = element.to_alipay_dict()
            if hasattr(self.chat_configs, 'to_alipay_dict'):
                params['chat_configs'] = self.chat_configs.to_alipay_dict()
            else:
                params['chat_configs'] = self.chat_configs
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.hotline_configs:
            if isinstance(self.hotline_configs, list):
                for i in range(0, len(self.hotline_configs)):
                    element = self.hotline_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hotline_configs[i] = element.to_alipay_dict()
            if hasattr(self.hotline_configs, 'to_alipay_dict'):
                params['hotline_configs'] = self.hotline_configs.to_alipay_dict()
            else:
                params['hotline_configs'] = self.hotline_configs
        if self.job_number:
            if hasattr(self.job_number, 'to_alipay_dict'):
                params['job_number'] = self.job_number.to_alipay_dict()
            else:
                params['job_number'] = self.job_number
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.role_ids:
            if isinstance(self.role_ids, list):
                for i in range(0, len(self.role_ids)):
                    element = self.role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_ids[i] = element.to_alipay_dict()
            if hasattr(self.role_ids, 'to_alipay_dict'):
                params['role_ids'] = self.role_ids.to_alipay_dict()
            else:
                params['role_ids'] = self.role_ids
        if self.user_channel:
            if hasattr(self.user_channel, 'to_alipay_dict'):
                params['user_channel'] = self.user_channel.to_alipay_dict()
            else:
                params['user_channel'] = self.user_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmAgentCreateModel()
        if 'answering_mode' in d:
            o.answering_mode = d['answering_mode']
        if 'ccs_instance_ids' in d:
            o.ccs_instance_ids = d['ccs_instance_ids']
        if 'chat_configs' in d:
            o.chat_configs = d['chat_configs']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'email' in d:
            o.email = d['email']
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'hotline_configs' in d:
            o.hotline_configs = d['hotline_configs']
        if 'job_number' in d:
            o.job_number = d['job_number']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'role_ids' in d:
            o.role_ids = d['role_ids']
        if 'user_channel' in d:
            o.user_channel = d['user_channel']
        return o


