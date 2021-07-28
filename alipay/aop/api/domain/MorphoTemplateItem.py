#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoUser import MorphoUser


class MorphoTemplateItem(object):

    def __init__(self):
        self._gmt_modified = None
        self._name = None
        self._owner = None
        self._snapshot = None
        self._summary = None
        self._template_version = None
        self._title = None

    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def snapshot(self):
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.snapshot:
            if hasattr(self.snapshot, 'to_alipay_dict'):
                params['snapshot'] = self.snapshot.to_alipay_dict()
            else:
                params['snapshot'] = self.snapshot
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
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
        o = MorphoTemplateItem()
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'name' in d:
            o.name = d['name']
        if 'owner' in d:
            o.owner = d['owner']
        if 'snapshot' in d:
            o.snapshot = d['snapshot']
        if 'summary' in d:
            o.summary = d['summary']
        if 'template_version' in d:
            o.template_version = d['template_version']
        if 'title' in d:
            o.title = d['title']
        return o


