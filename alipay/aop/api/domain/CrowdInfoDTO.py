#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdInfoDTO(object):

    def __init__(self):
        self._create_time = None
        self._creator_name = None
        self._crowd_name = None
        self._crowd_num = None
        self._effective_time = None
        self._ext_crowd_key = None
        self._id = None
        self._status = None
        self._update_time = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def crowd_num(self):
        return self._crowd_num

    @crowd_num.setter
    def crowd_num(self, value):
        self._crowd_num = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def ext_crowd_key(self):
        return self._ext_crowd_key

    @ext_crowd_key.setter
    def ext_crowd_key(self, value):
        self._ext_crowd_key = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.crowd_num:
            if hasattr(self.crowd_num, 'to_alipay_dict'):
                params['crowd_num'] = self.crowd_num.to_alipay_dict()
            else:
                params['crowd_num'] = self.crowd_num
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.ext_crowd_key:
            if hasattr(self.ext_crowd_key, 'to_alipay_dict'):
                params['ext_crowd_key'] = self.ext_crowd_key.to_alipay_dict()
            else:
                params['ext_crowd_key'] = self.ext_crowd_key
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdInfoDTO()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'crowd_num' in d:
            o.crowd_num = d['crowd_num']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'ext_crowd_key' in d:
            o.ext_crowd_key = d['ext_crowd_key']
        if 'id' in d:
            o.id = d['id']
        if 'status' in d:
            o.status = d['status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


