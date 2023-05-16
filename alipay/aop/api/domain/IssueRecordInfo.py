#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IssueRecordInfo(object):

    def __init__(self):
        self._issue_quota = None
        self._issue_status = None
        self._owner_id = None
        self._owner_open_id = None
        self._owner_type = None
        self._quota_id = None
        self._user_name = None

    @property
    def issue_quota(self):
        return self._issue_quota

    @issue_quota.setter
    def issue_quota(self, value):
        self._issue_quota = value
    @property
    def issue_status(self):
        return self._issue_status

    @issue_status.setter
    def issue_status(self, value):
        self._issue_status = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_open_id(self):
        return self._owner_open_id

    @owner_open_id.setter
    def owner_open_id(self, value):
        self._owner_open_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def quota_id(self):
        return self._quota_id

    @quota_id.setter
    def quota_id(self, value):
        self._quota_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.issue_quota:
            if hasattr(self.issue_quota, 'to_alipay_dict'):
                params['issue_quota'] = self.issue_quota.to_alipay_dict()
            else:
                params['issue_quota'] = self.issue_quota
        if self.issue_status:
            if hasattr(self.issue_status, 'to_alipay_dict'):
                params['issue_status'] = self.issue_status.to_alipay_dict()
            else:
                params['issue_status'] = self.issue_status
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_open_id:
            if hasattr(self.owner_open_id, 'to_alipay_dict'):
                params['owner_open_id'] = self.owner_open_id.to_alipay_dict()
            else:
                params['owner_open_id'] = self.owner_open_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.quota_id:
            if hasattr(self.quota_id, 'to_alipay_dict'):
                params['quota_id'] = self.quota_id.to_alipay_dict()
            else:
                params['quota_id'] = self.quota_id
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
        o = IssueRecordInfo()
        if 'issue_quota' in d:
            o.issue_quota = d['issue_quota']
        if 'issue_status' in d:
            o.issue_status = d['issue_status']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_open_id' in d:
            o.owner_open_id = d['owner_open_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'quota_id' in d:
            o.quota_id = d['quota_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


