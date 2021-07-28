#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgentChatInfo import AgentChatInfo
from alipay.aop.api.domain.AgentHotlineInfo import AgentHotlineInfo
from alipay.aop.api.domain.RoleId import RoleId


class AlipayIserviceCcmAgentGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmAgentGetResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmAgentGetResponse, self).parse_response_content(response_content)
        if 'answering_mode' in response:
            self.answering_mode = response['answering_mode']
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'ccs_instance_ids' in response:
            self.ccs_instance_ids = response['ccs_instance_ids']
        if 'chat_config' in response:
            self.chat_config = response['chat_config']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'creator_id' in response:
            self.creator_id = response['creator_id']
        if 'dingtalk_user_id' in response:
            self.dingtalk_user_id = response['dingtalk_user_id']
        if 'email' in response:
            self.email = response['email']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'hotline_config' in response:
            self.hotline_config = response['hotline_config']
        if 'id' in response:
            self.id = response['id']
        if 'job_number' in response:
            self.job_number = response['job_number']
        if 'last_login_time' in response:
            self.last_login_time = response['last_login_time']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'profile' in response:
            self.profile = response['profile']
        if 'real_name' in response:
            self.real_name = response['real_name']
        if 'role_ids' in response:
            self.role_ids = response['role_ids']
        if 'status' in response:
            self.status = response['status']
        if 'type' in response:
            self.type = response['type']
        if 'update_time' in response:
            self.update_time = response['update_time']
        if 'updater_id' in response:
            self.updater_id = response['updater_id']
