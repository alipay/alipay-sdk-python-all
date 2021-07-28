#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlegalchainEcsealApplyModel(object):

    def __init__(self):
        self._bas_data_id = None
        self._biz_unique_id = None
        self._file_name = None
        self._file_uniq_id = None
        self._notify_emails = None
        self._request_app_name = None
        self._request_time_stamp = None
        self._request_token = None
        self._task_owner_email = None
        self._task_owner_name = None
        self._task_owner_no = None

    @property
    def bas_data_id(self):
        return self._bas_data_id

    @bas_data_id.setter
    def bas_data_id(self, value):
        self._bas_data_id = value
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_uniq_id(self):
        return self._file_uniq_id

    @file_uniq_id.setter
    def file_uniq_id(self, value):
        self._file_uniq_id = value
    @property
    def notify_emails(self):
        return self._notify_emails

    @notify_emails.setter
    def notify_emails(self, value):
        if isinstance(value, list):
            self._notify_emails = list()
            for i in value:
                self._notify_emails.append(i)
    @property
    def request_app_name(self):
        return self._request_app_name

    @request_app_name.setter
    def request_app_name(self, value):
        self._request_app_name = value
    @property
    def request_time_stamp(self):
        return self._request_time_stamp

    @request_time_stamp.setter
    def request_time_stamp(self, value):
        self._request_time_stamp = value
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value
    @property
    def task_owner_email(self):
        return self._task_owner_email

    @task_owner_email.setter
    def task_owner_email(self, value):
        self._task_owner_email = value
    @property
    def task_owner_name(self):
        return self._task_owner_name

    @task_owner_name.setter
    def task_owner_name(self, value):
        self._task_owner_name = value
    @property
    def task_owner_no(self):
        return self._task_owner_no

    @task_owner_no.setter
    def task_owner_no(self, value):
        self._task_owner_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bas_data_id:
            if hasattr(self.bas_data_id, 'to_alipay_dict'):
                params['bas_data_id'] = self.bas_data_id.to_alipay_dict()
            else:
                params['bas_data_id'] = self.bas_data_id
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_uniq_id:
            if hasattr(self.file_uniq_id, 'to_alipay_dict'):
                params['file_uniq_id'] = self.file_uniq_id.to_alipay_dict()
            else:
                params['file_uniq_id'] = self.file_uniq_id
        if self.notify_emails:
            if isinstance(self.notify_emails, list):
                for i in range(0, len(self.notify_emails)):
                    element = self.notify_emails[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notify_emails[i] = element.to_alipay_dict()
            if hasattr(self.notify_emails, 'to_alipay_dict'):
                params['notify_emails'] = self.notify_emails.to_alipay_dict()
            else:
                params['notify_emails'] = self.notify_emails
        if self.request_app_name:
            if hasattr(self.request_app_name, 'to_alipay_dict'):
                params['request_app_name'] = self.request_app_name.to_alipay_dict()
            else:
                params['request_app_name'] = self.request_app_name
        if self.request_time_stamp:
            if hasattr(self.request_time_stamp, 'to_alipay_dict'):
                params['request_time_stamp'] = self.request_time_stamp.to_alipay_dict()
            else:
                params['request_time_stamp'] = self.request_time_stamp
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        if self.task_owner_email:
            if hasattr(self.task_owner_email, 'to_alipay_dict'):
                params['task_owner_email'] = self.task_owner_email.to_alipay_dict()
            else:
                params['task_owner_email'] = self.task_owner_email
        if self.task_owner_name:
            if hasattr(self.task_owner_name, 'to_alipay_dict'):
                params['task_owner_name'] = self.task_owner_name.to_alipay_dict()
            else:
                params['task_owner_name'] = self.task_owner_name
        if self.task_owner_no:
            if hasattr(self.task_owner_no, 'to_alipay_dict'):
                params['task_owner_no'] = self.task_owner_no.to_alipay_dict()
            else:
                params['task_owner_no'] = self.task_owner_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlegalchainEcsealApplyModel()
        if 'bas_data_id' in d:
            o.bas_data_id = d['bas_data_id']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_uniq_id' in d:
            o.file_uniq_id = d['file_uniq_id']
        if 'notify_emails' in d:
            o.notify_emails = d['notify_emails']
        if 'request_app_name' in d:
            o.request_app_name = d['request_app_name']
        if 'request_time_stamp' in d:
            o.request_time_stamp = d['request_time_stamp']
        if 'request_token' in d:
            o.request_token = d['request_token']
        if 'task_owner_email' in d:
            o.task_owner_email = d['task_owner_email']
        if 'task_owner_name' in d:
            o.task_owner_name = d['task_owner_name']
        if 'task_owner_no' in d:
            o.task_owner_no = d['task_owner_no']
        return o


