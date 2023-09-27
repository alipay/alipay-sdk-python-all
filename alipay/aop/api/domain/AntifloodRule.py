#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntifloodRule(object):

    def __init__(self):
        self._cidr_block = None
        self._end = None
        self._gmt_create = None
        self._gmt_modified = None
        self._source = None
        self._start = None

    @property
    def cidr_block(self):
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, value):
        self._cidr_block = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value


    def to_alipay_dict(self):
        params = dict()
        if self.cidr_block:
            if hasattr(self.cidr_block, 'to_alipay_dict'):
                params['cidr_block'] = self.cidr_block.to_alipay_dict()
            else:
                params['cidr_block'] = self.cidr_block
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntifloodRule()
        if 'cidr_block' in d:
            o.cidr_block = d['cidr_block']
        if 'end' in d:
            o.end = d['end']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'source' in d:
            o.source = d['source']
        if 'start' in d:
            o.start = d['start']
        return o


