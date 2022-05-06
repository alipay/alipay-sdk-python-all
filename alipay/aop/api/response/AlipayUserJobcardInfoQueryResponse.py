#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserJobcardInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserJobcardInfoQueryResponse, self).__init__()
        self._admin_area = None
        self._gender = None
        self._intent_post_tag = None
        self._job_site_type = None
        self._job_time_type = None
        self._local_range = None
        self._skill_tag = None
        self._suitable_age_status = None
        self._user_age = None
        self._user_name = None
        self._user_phone = None

    @property
    def admin_area(self):
        return self._admin_area

    @admin_area.setter
    def admin_area(self, value):
        self._admin_area = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def intent_post_tag(self):
        return self._intent_post_tag

    @intent_post_tag.setter
    def intent_post_tag(self, value):
        self._intent_post_tag = value
    @property
    def job_site_type(self):
        return self._job_site_type

    @job_site_type.setter
    def job_site_type(self, value):
        self._job_site_type = value
    @property
    def job_time_type(self):
        return self._job_time_type

    @job_time_type.setter
    def job_time_type(self, value):
        self._job_time_type = value
    @property
    def local_range(self):
        return self._local_range

    @local_range.setter
    def local_range(self, value):
        self._local_range = value
    @property
    def skill_tag(self):
        return self._skill_tag

    @skill_tag.setter
    def skill_tag(self, value):
        self._skill_tag = value
    @property
    def suitable_age_status(self):
        return self._suitable_age_status

    @suitable_age_status.setter
    def suitable_age_status(self, value):
        self._suitable_age_status = value
    @property
    def user_age(self):
        return self._user_age

    @user_age.setter
    def user_age(self, value):
        self._user_age = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserJobcardInfoQueryResponse, self).parse_response_content(response_content)
        if 'admin_area' in response:
            self.admin_area = response['admin_area']
        if 'gender' in response:
            self.gender = response['gender']
        if 'intent_post_tag' in response:
            self.intent_post_tag = response['intent_post_tag']
        if 'job_site_type' in response:
            self.job_site_type = response['job_site_type']
        if 'job_time_type' in response:
            self.job_time_type = response['job_time_type']
        if 'local_range' in response:
            self.local_range = response['local_range']
        if 'skill_tag' in response:
            self.skill_tag = response['skill_tag']
        if 'suitable_age_status' in response:
            self.suitable_age_status = response['suitable_age_status']
        if 'user_age' in response:
            self.user_age = response['user_age']
        if 'user_name' in response:
            self.user_name = response['user_name']
        if 'user_phone' in response:
            self.user_phone = response['user_phone']
