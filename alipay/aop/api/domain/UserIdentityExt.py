#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserIdentityExt(object):

    def __init__(self):
        self._account_issue_entity_id = None
        self._account_issue_entity_name = None
        self._account_name = None
        self._account_no = None
        self._ext_info = None
        self._inst_uuid = None
        self._inst_uuid_type = None
        self._member_id = None
        self._member_name = None

    @property
    def account_issue_entity_id(self):
        return self._account_issue_entity_id

    @account_issue_entity_id.setter
    def account_issue_entity_id(self, value):
        self._account_issue_entity_id = value
    @property
    def account_issue_entity_name(self):
        return self._account_issue_entity_name

    @account_issue_entity_name.setter
    def account_issue_entity_name(self, value):
        self._account_issue_entity_name = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def inst_uuid(self):
        return self._inst_uuid

    @inst_uuid.setter
    def inst_uuid(self, value):
        self._inst_uuid = value
    @property
    def inst_uuid_type(self):
        return self._inst_uuid_type

    @inst_uuid_type.setter
    def inst_uuid_type(self, value):
        self._inst_uuid_type = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_issue_entity_id:
            if hasattr(self.account_issue_entity_id, 'to_alipay_dict'):
                params['account_issue_entity_id'] = self.account_issue_entity_id.to_alipay_dict()
            else:
                params['account_issue_entity_id'] = self.account_issue_entity_id
        if self.account_issue_entity_name:
            if hasattr(self.account_issue_entity_name, 'to_alipay_dict'):
                params['account_issue_entity_name'] = self.account_issue_entity_name.to_alipay_dict()
            else:
                params['account_issue_entity_name'] = self.account_issue_entity_name
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inst_uuid:
            if hasattr(self.inst_uuid, 'to_alipay_dict'):
                params['inst_uuid'] = self.inst_uuid.to_alipay_dict()
            else:
                params['inst_uuid'] = self.inst_uuid
        if self.inst_uuid_type:
            if hasattr(self.inst_uuid_type, 'to_alipay_dict'):
                params['inst_uuid_type'] = self.inst_uuid_type.to_alipay_dict()
            else:
                params['inst_uuid_type'] = self.inst_uuid_type
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.member_name:
            if hasattr(self.member_name, 'to_alipay_dict'):
                params['member_name'] = self.member_name.to_alipay_dict()
            else:
                params['member_name'] = self.member_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserIdentityExt()
        if 'account_issue_entity_id' in d:
            o.account_issue_entity_id = d['account_issue_entity_id']
        if 'account_issue_entity_name' in d:
            o.account_issue_entity_name = d['account_issue_entity_name']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inst_uuid' in d:
            o.inst_uuid = d['inst_uuid']
        if 'inst_uuid_type' in d:
            o.inst_uuid_type = d['inst_uuid_type']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'member_name' in d:
            o.member_name = d['member_name']
        return o


