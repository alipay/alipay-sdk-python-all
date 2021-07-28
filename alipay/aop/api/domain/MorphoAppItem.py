#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoMiniMeta import MorphoMiniMeta
from alipay.aop.api.domain.MorphoUser import MorphoUser


class MorphoAppItem(object):

    def __init__(self):
        self._gmt_modified = None
        self._id = None
        self._mini_meta = None
        self._online_state = None
        self._owner = None
        self._status = None
        self._title = None
        self._type = None

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
    def mini_meta(self):
        return self._mini_meta

    @mini_meta.setter
    def mini_meta(self, value):
        if isinstance(value, MorphoMiniMeta):
            self._mini_meta = value
        else:
            self._mini_meta = MorphoMiniMeta.from_alipay_dict(value)
    @property
    def online_state(self):
        return self._online_state

    @online_state.setter
    def online_state(self, value):
        self._online_state = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, MorphoUser):
            self._owner = value
        else:
            self._owner = MorphoUser.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


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
        if self.mini_meta:
            if hasattr(self.mini_meta, 'to_alipay_dict'):
                params['mini_meta'] = self.mini_meta.to_alipay_dict()
            else:
                params['mini_meta'] = self.mini_meta
        if self.online_state:
            if hasattr(self.online_state, 'to_alipay_dict'):
                params['online_state'] = self.online_state.to_alipay_dict()
            else:
                params['online_state'] = self.online_state
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
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MorphoAppItem()
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'mini_meta' in d:
            o.mini_meta = d['mini_meta']
        if 'online_state' in d:
            o.online_state = d['online_state']
        if 'owner' in d:
            o.owner = d['owner']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


