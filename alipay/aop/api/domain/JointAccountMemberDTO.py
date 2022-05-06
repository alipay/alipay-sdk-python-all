#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JointAccountQuotaDTO import JointAccountQuotaDTO
from alipay.aop.api.domain.MemberExtInfo import MemberExtInfo


class JointAccountMemberDTO(object):

    def __init__(self):
        self._account_quota = None
        self._member_ext_info = None
        self._name = None
        self._status = None
        self._user_id = None

    @property
    def account_quota(self):
        return self._account_quota

    @account_quota.setter
    def account_quota(self, value):
        if isinstance(value, JointAccountQuotaDTO):
            self._account_quota = value
        else:
            self._account_quota = JointAccountQuotaDTO.from_alipay_dict(value)
    @property
    def member_ext_info(self):
        return self._member_ext_info

    @member_ext_info.setter
    def member_ext_info(self, value):
        if isinstance(value, MemberExtInfo):
            self._member_ext_info = value
        else:
            self._member_ext_info = MemberExtInfo.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_quota:
            if hasattr(self.account_quota, 'to_alipay_dict'):
                params['account_quota'] = self.account_quota.to_alipay_dict()
            else:
                params['account_quota'] = self.account_quota
        if self.member_ext_info:
            if hasattr(self.member_ext_info, 'to_alipay_dict'):
                params['member_ext_info'] = self.member_ext_info.to_alipay_dict()
            else:
                params['member_ext_info'] = self.member_ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JointAccountMemberDTO()
        if 'account_quota' in d:
            o.account_quota = d['account_quota']
        if 'member_ext_info' in d:
            o.member_ext_info = d['member_ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


