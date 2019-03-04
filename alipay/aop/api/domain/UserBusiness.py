#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserBusiness(object):

    def __init__(self):
        self._access_level = None
        self._business_desc = None
        self._business_id = None
        self._business_name = None
        self._business_remark = None
        self._business_status = None
        self._owner = None
        self._user_status = None

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, value):
        self._access_level = value
    @property
    def business_desc(self):
        return self._business_desc

    @business_desc.setter
    def business_desc(self, value):
        self._business_desc = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value
    @property
    def business_remark(self):
        return self._business_remark

    @business_remark.setter
    def business_remark(self, value):
        self._business_remark = value
    @property
    def business_status(self):
        return self._business_status

    @business_status.setter
    def business_status(self, value):
        self._business_status = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_level:
            if hasattr(self.access_level, 'to_alipay_dict'):
                params['access_level'] = self.access_level.to_alipay_dict()
            else:
                params['access_level'] = self.access_level
        if self.business_desc:
            if hasattr(self.business_desc, 'to_alipay_dict'):
                params['business_desc'] = self.business_desc.to_alipay_dict()
            else:
                params['business_desc'] = self.business_desc
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.business_name:
            if hasattr(self.business_name, 'to_alipay_dict'):
                params['business_name'] = self.business_name.to_alipay_dict()
            else:
                params['business_name'] = self.business_name
        if self.business_remark:
            if hasattr(self.business_remark, 'to_alipay_dict'):
                params['business_remark'] = self.business_remark.to_alipay_dict()
            else:
                params['business_remark'] = self.business_remark
        if self.business_status:
            if hasattr(self.business_status, 'to_alipay_dict'):
                params['business_status'] = self.business_status.to_alipay_dict()
            else:
                params['business_status'] = self.business_status
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.user_status:
            if hasattr(self.user_status, 'to_alipay_dict'):
                params['user_status'] = self.user_status.to_alipay_dict()
            else:
                params['user_status'] = self.user_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserBusiness()
        if 'access_level' in d:
            o.access_level = d['access_level']
        if 'business_desc' in d:
            o.business_desc = d['business_desc']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_name' in d:
            o.business_name = d['business_name']
        if 'business_remark' in d:
            o.business_remark = d['business_remark']
        if 'business_status' in d:
            o.business_status = d['business_status']
        if 'owner' in d:
            o.owner = d['owner']
        if 'user_status' in d:
            o.user_status = d['user_status']
        return o


