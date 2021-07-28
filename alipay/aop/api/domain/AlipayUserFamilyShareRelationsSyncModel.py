#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserFamilyShareRelationsSyncModel(object):

    def __init__(self):
        self._expired_date = None
        self._resource_content = None
        self._resource_id = None
        self._scene_id = None
        self._sharing_user_ids = None
        self._sharing_user_type = None
        self._target_status = None
        self._update_date = None
        self._user_id = None
        self._version_no = None

    @property
    def expired_date(self):
        return self._expired_date

    @expired_date.setter
    def expired_date(self, value):
        self._expired_date = value
    @property
    def resource_content(self):
        return self._resource_content

    @resource_content.setter
    def resource_content(self, value):
        self._resource_content = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def sharing_user_ids(self):
        return self._sharing_user_ids

    @sharing_user_ids.setter
    def sharing_user_ids(self, value):
        if isinstance(value, list):
            self._sharing_user_ids = list()
            for i in value:
                self._sharing_user_ids.append(i)
    @property
    def sharing_user_type(self):
        return self._sharing_user_type

    @sharing_user_type.setter
    def sharing_user_type(self, value):
        self._sharing_user_type = value
    @property
    def target_status(self):
        return self._target_status

    @target_status.setter
    def target_status(self, value):
        self._target_status = value
    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_date:
            if hasattr(self.expired_date, 'to_alipay_dict'):
                params['expired_date'] = self.expired_date.to_alipay_dict()
            else:
                params['expired_date'] = self.expired_date
        if self.resource_content:
            if hasattr(self.resource_content, 'to_alipay_dict'):
                params['resource_content'] = self.resource_content.to_alipay_dict()
            else:
                params['resource_content'] = self.resource_content
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.sharing_user_ids:
            if isinstance(self.sharing_user_ids, list):
                for i in range(0, len(self.sharing_user_ids)):
                    element = self.sharing_user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sharing_user_ids[i] = element.to_alipay_dict()
            if hasattr(self.sharing_user_ids, 'to_alipay_dict'):
                params['sharing_user_ids'] = self.sharing_user_ids.to_alipay_dict()
            else:
                params['sharing_user_ids'] = self.sharing_user_ids
        if self.sharing_user_type:
            if hasattr(self.sharing_user_type, 'to_alipay_dict'):
                params['sharing_user_type'] = self.sharing_user_type.to_alipay_dict()
            else:
                params['sharing_user_type'] = self.sharing_user_type
        if self.target_status:
            if hasattr(self.target_status, 'to_alipay_dict'):
                params['target_status'] = self.target_status.to_alipay_dict()
            else:
                params['target_status'] = self.target_status
        if self.update_date:
            if hasattr(self.update_date, 'to_alipay_dict'):
                params['update_date'] = self.update_date.to_alipay_dict()
            else:
                params['update_date'] = self.update_date
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserFamilyShareRelationsSyncModel()
        if 'expired_date' in d:
            o.expired_date = d['expired_date']
        if 'resource_content' in d:
            o.resource_content = d['resource_content']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'sharing_user_ids' in d:
            o.sharing_user_ids = d['sharing_user_ids']
        if 'sharing_user_type' in d:
            o.sharing_user_type = d['sharing_user_type']
        if 'target_status' in d:
            o.target_status = d['target_status']
        if 'update_date' in d:
            o.update_date = d['update_date']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


