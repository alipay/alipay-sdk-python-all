#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FengdieTemplateDetailModel(object):

    def __init__(self):
        self._id = None
        self._maintainer = None
        self._name = None
        self._owner = None
        self._snapshot = None
        self._summary = None
        self._title = None
        self._ver = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def maintainer(self):
        return self._maintainer

    @maintainer.setter
    def maintainer(self, value):
        if isinstance(value, list):
            self._maintainer = list()
            for i in value:
                self._maintainer.append(i)
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
        self._owner = value
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def ver(self):
        return self._ver

    @ver.setter
    def ver(self, value):
        self._ver = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.maintainer:
            if isinstance(self.maintainer, list):
                for i in range(0, len(self.maintainer)):
                    element = self.maintainer[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.maintainer[i] = element.to_alipay_dict()
            if hasattr(self.maintainer, 'to_alipay_dict'):
                params['maintainer'] = self.maintainer.to_alipay_dict()
            else:
                params['maintainer'] = self.maintainer
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
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.ver:
            if hasattr(self.ver, 'to_alipay_dict'):
                params['ver'] = self.ver.to_alipay_dict()
            else:
                params['ver'] = self.ver
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieTemplateDetailModel()
        if 'id' in d:
            o.id = d['id']
        if 'maintainer' in d:
            o.maintainer = d['maintainer']
        if 'name' in d:
            o.name = d['name']
        if 'owner' in d:
            o.owner = d['owner']
        if 'snapshot' in d:
            o.snapshot = d['snapshot']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        if 'ver' in d:
            o.ver = d['ver']
        return o


