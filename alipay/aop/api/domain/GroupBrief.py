#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupBrief(object):

    def __init__(self):
        self._gmt_create = None
        self._group_id = None
        self._group_img = None
        self._group_name = None
        self._master_uid = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_img(self):
        return self._group_img

    @group_img.setter
    def group_img(self, value):
        self._group_img = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def master_uid(self):
        return self._master_uid

    @master_uid.setter
    def master_uid(self, value):
        self._master_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_img:
            if hasattr(self.group_img, 'to_alipay_dict'):
                params['group_img'] = self.group_img.to_alipay_dict()
            else:
                params['group_img'] = self.group_img
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.master_uid:
            if hasattr(self.master_uid, 'to_alipay_dict'):
                params['master_uid'] = self.master_uid.to_alipay_dict()
            else:
                params['master_uid'] = self.master_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupBrief()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_img' in d:
            o.group_img = d['group_img']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'master_uid' in d:
            o.master_uid = d['master_uid']
        return o


