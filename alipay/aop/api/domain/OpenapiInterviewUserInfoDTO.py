#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenapiInterviewUserInfoDTO(object):

    def __init__(self):
        self._user_education_info = None
        self._user_email = None
        self._user_mobile = None
        self._user_name = None
        self._user_project_experience = None
        self._user_resume_url = None

    @property
    def user_education_info(self):
        return self._user_education_info

    @user_education_info.setter
    def user_education_info(self, value):
        self._user_education_info = value
    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_project_experience(self):
        return self._user_project_experience

    @user_project_experience.setter
    def user_project_experience(self, value):
        self._user_project_experience = value
    @property
    def user_resume_url(self):
        return self._user_resume_url

    @user_resume_url.setter
    def user_resume_url(self, value):
        self._user_resume_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_education_info:
            if hasattr(self.user_education_info, 'to_alipay_dict'):
                params['user_education_info'] = self.user_education_info.to_alipay_dict()
            else:
                params['user_education_info'] = self.user_education_info
        if self.user_email:
            if hasattr(self.user_email, 'to_alipay_dict'):
                params['user_email'] = self.user_email.to_alipay_dict()
            else:
                params['user_email'] = self.user_email
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_project_experience:
            if hasattr(self.user_project_experience, 'to_alipay_dict'):
                params['user_project_experience'] = self.user_project_experience.to_alipay_dict()
            else:
                params['user_project_experience'] = self.user_project_experience
        if self.user_resume_url:
            if hasattr(self.user_resume_url, 'to_alipay_dict'):
                params['user_resume_url'] = self.user_resume_url.to_alipay_dict()
            else:
                params['user_resume_url'] = self.user_resume_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenapiInterviewUserInfoDTO()
        if 'user_education_info' in d:
            o.user_education_info = d['user_education_info']
        if 'user_email' in d:
            o.user_email = d['user_email']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_project_experience' in d:
            o.user_project_experience = d['user_project_experience']
        if 'user_resume_url' in d:
            o.user_resume_url = d['user_resume_url']
        return o


