#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlescenterDocusignrecipientQueryModel(object):

    def __init__(self):
        self._app_name = None
        self._back_url = None
        self._biz_no = None
        self._email = None
        self._recipient_id = None
        self._sign_task_id = None
        self._user_name = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def recipient_id(self):
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, value):
        self._recipient_id = value
    @property
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.recipient_id:
            if hasattr(self.recipient_id, 'to_alipay_dict'):
                params['recipient_id'] = self.recipient_id.to_alipay_dict()
            else:
                params['recipient_id'] = self.recipient_id
        if self.sign_task_id:
            if hasattr(self.sign_task_id, 'to_alipay_dict'):
                params['sign_task_id'] = self.sign_task_id.to_alipay_dict()
            else:
                params['sign_task_id'] = self.sign_task_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlescenterDocusignrecipientQueryModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'email' in d:
            o.email = d['email']
        if 'recipient_id' in d:
            o.recipient_id = d['recipient_id']
        if 'sign_task_id' in d:
            o.sign_task_id = d['sign_task_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


