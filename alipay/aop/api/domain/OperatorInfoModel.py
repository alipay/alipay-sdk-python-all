#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorInfoModel(object):

    def __init__(self):
        self._cid = None
        self._email = None
        self._job_id = None
        self._job_tree = None
        self._mobile = None
        self._name = None
        self._nick_name = None
        self._operator_id = None
        self._operator_type = None
        self._role_id = None
        self._role_name = None
        self._shop_ids = None
        self._status = None

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_tree(self):
        return self._job_tree

    @job_tree.setter
    def job_tree(self, value):
        self._job_tree = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_tree:
            if hasattr(self.job_tree, 'to_alipay_dict'):
                params['job_tree'] = self.job_tree.to_alipay_dict()
            else:
                params['job_tree'] = self.job_tree
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.role_id:
            if hasattr(self.role_id, 'to_alipay_dict'):
                params['role_id'] = self.role_id.to_alipay_dict()
            else:
                params['role_id'] = self.role_id
        if self.role_name:
            if hasattr(self.role_name, 'to_alipay_dict'):
                params['role_name'] = self.role_name.to_alipay_dict()
            else:
                params['role_name'] = self.role_name
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorInfoModel()
        if 'cid' in d:
            o.cid = d['cid']
        if 'email' in d:
            o.email = d['email']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_tree' in d:
            o.job_tree = d['job_tree']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'role_id' in d:
            o.role_id = d['role_id']
        if 'role_name' in d:
            o.role_name = d['role_name']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'status' in d:
            o.status = d['status']
        return o


