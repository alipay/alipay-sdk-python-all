#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieSitesOwner import FengdieSitesOwner


class FengdieSitesListModel(object):

    def __init__(self):
        self._gmt_modified = None
        self._id = None
        self._is_online = None
        self._offline_time = None
        self._owner = None
        self._status = None
        self._template_name = None
        self._template_version = None
        self._title = None

    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def offline_time(self):
        return self._offline_time

    @offline_time.setter
    def offline_time(self, value):
        self._offline_time = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, FengdieSitesOwner):
            self._owner = value
        else:
            self._owner = FengdieSitesOwner.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_online:
            if hasattr(self.is_online, 'to_alipay_dict'):
                params['is_online'] = self.is_online.to_alipay_dict()
            else:
                params['is_online'] = self.is_online
        if self.offline_time:
            if hasattr(self.offline_time, 'to_alipay_dict'):
                params['offline_time'] = self.offline_time.to_alipay_dict()
            else:
                params['offline_time'] = self.offline_time
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieSitesListModel()
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'is_online' in d:
            o.is_online = d['is_online']
        if 'offline_time' in d:
            o.offline_time = d['offline_time']
        if 'owner' in d:
            o.owner = d['owner']
        if 'status' in d:
            o.status = d['status']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'template_version' in d:
            o.template_version = d['template_version']
        if 'title' in d:
            o.title = d['title']
        return o


