#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupPromoteChannelVO(object):

    def __init__(self):
        self._delete_tag = None
        self._desc = None
        self._id = None
        self._key = None
        self._name = None
        self._promote_link = None

    @property
    def delete_tag(self):
        return self._delete_tag

    @delete_tag.setter
    def delete_tag(self, value):
        self._delete_tag = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def promote_link(self):
        return self._promote_link

    @promote_link.setter
    def promote_link(self, value):
        self._promote_link = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_tag:
            if hasattr(self.delete_tag, 'to_alipay_dict'):
                params['delete_tag'] = self.delete_tag.to_alipay_dict()
            else:
                params['delete_tag'] = self.delete_tag
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.promote_link:
            if hasattr(self.promote_link, 'to_alipay_dict'):
                params['promote_link'] = self.promote_link.to_alipay_dict()
            else:
                params['promote_link'] = self.promote_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPromoteChannelVO()
        if 'delete_tag' in d:
            o.delete_tag = d['delete_tag']
        if 'desc' in d:
            o.desc = d['desc']
        if 'id' in d:
            o.id = d['id']
        if 'key' in d:
            o.key = d['key']
        if 'name' in d:
            o.name = d['name']
        if 'promote_link' in d:
            o.promote_link = d['promote_link']
        return o


