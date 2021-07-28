#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgentChatInfo import AgentChatInfo
from alipay.aop.api.domain.AgentHotlineInfo import AgentHotlineInfo
from alipay.aop.api.domain.RoleId import RoleId


class AgentVO(object):

    def __init__(self):
        self._answering_mode = None
        self._avatar = None
        self._ccs_instance_ids = None
        self._chat_config = None
        self._create_time = None
        self._creator_id = None
        self._dingtalk_user_id = None
        self._email = None
        self._external_id = None
        self._hotline_config = None
        self._id = None
        self._job_number = None
        self._last_login_time = None
        self._mobile = None
        self._nick_name = None
        self._profile = None
        self._real_name = None
        self._role_ids = None
        self._status = None
        self._type = None
        self._update_time = None
        self._updater_id = None

    @property
    def answering_mode(self):
        return self._answering_mode

    @answering_mode.setter
    def answering_mode(self, value):
        self._answering_mode = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
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
    def chat_config(self):
        return self._chat_config

    @chat_config.setter
    def chat_config(self, value):
        if isinstance(value, list):
            self._chat_config = list()
            for i in value:
                if isinstance(i, AgentChatInfo):
                    self._chat_config.append(i)
                else:
                    self._chat_config.append(AgentChatInfo.from_alipay_dict(i))
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def dingtalk_user_id(self):
        return self._dingtalk_user_id

    @dingtalk_user_id.setter
    def dingtalk_user_id(self, value):
        self._dingtalk_user_id = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def hotline_config(self):
        return self._hotline_config

    @hotline_config.setter
    def hotline_config(self, value):
        if isinstance(value, list):
            self._hotline_config = list()
            for i in value:
                if isinstance(i, AgentHotlineInfo):
                    self._hotline_config.append(i)
                else:
                    self._hotline_config.append(AgentHotlineInfo.from_alipay_dict(i))
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def job_number(self):
        return self._job_number

    @job_number.setter
    def job_number(self, value):
        self._job_number = value
    @property
    def last_login_time(self):
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, value):
        self._last_login_time = value
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
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, value):
        self._profile = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def updater_id(self):
        return self._updater_id

    @updater_id.setter
    def updater_id(self, value):
        self._updater_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.answering_mode:
            if hasattr(self.answering_mode, 'to_alipay_dict'):
                params['answering_mode'] = self.answering_mode.to_alipay_dict()
            else:
                params['answering_mode'] = self.answering_mode
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
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
        if self.chat_config:
            if isinstance(self.chat_config, list):
                for i in range(0, len(self.chat_config)):
                    element = self.chat_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.chat_config[i] = element.to_alipay_dict()
            if hasattr(self.chat_config, 'to_alipay_dict'):
                params['chat_config'] = self.chat_config.to_alipay_dict()
            else:
                params['chat_config'] = self.chat_config
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.dingtalk_user_id:
            if hasattr(self.dingtalk_user_id, 'to_alipay_dict'):
                params['dingtalk_user_id'] = self.dingtalk_user_id.to_alipay_dict()
            else:
                params['dingtalk_user_id'] = self.dingtalk_user_id
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.hotline_config:
            if isinstance(self.hotline_config, list):
                for i in range(0, len(self.hotline_config)):
                    element = self.hotline_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hotline_config[i] = element.to_alipay_dict()
            if hasattr(self.hotline_config, 'to_alipay_dict'):
                params['hotline_config'] = self.hotline_config.to_alipay_dict()
            else:
                params['hotline_config'] = self.hotline_config
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.job_number:
            if hasattr(self.job_number, 'to_alipay_dict'):
                params['job_number'] = self.job_number.to_alipay_dict()
            else:
                params['job_number'] = self.job_number
        if self.last_login_time:
            if hasattr(self.last_login_time, 'to_alipay_dict'):
                params['last_login_time'] = self.last_login_time.to_alipay_dict()
            else:
                params['last_login_time'] = self.last_login_time
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
        if self.profile:
            if hasattr(self.profile, 'to_alipay_dict'):
                params['profile'] = self.profile.to_alipay_dict()
            else:
                params['profile'] = self.profile
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.updater_id:
            if hasattr(self.updater_id, 'to_alipay_dict'):
                params['updater_id'] = self.updater_id.to_alipay_dict()
            else:
                params['updater_id'] = self.updater_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentVO()
        if 'answering_mode' in d:
            o.answering_mode = d['answering_mode']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'ccs_instance_ids' in d:
            o.ccs_instance_ids = d['ccs_instance_ids']
        if 'chat_config' in d:
            o.chat_config = d['chat_config']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'dingtalk_user_id' in d:
            o.dingtalk_user_id = d['dingtalk_user_id']
        if 'email' in d:
            o.email = d['email']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'hotline_config' in d:
            o.hotline_config = d['hotline_config']
        if 'id' in d:
            o.id = d['id']
        if 'job_number' in d:
            o.job_number = d['job_number']
        if 'last_login_time' in d:
            o.last_login_time = d['last_login_time']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'profile' in d:
            o.profile = d['profile']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'role_ids' in d:
            o.role_ids = d['role_ids']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'updater_id' in d:
            o.updater_id = d['updater_id']
        return o


