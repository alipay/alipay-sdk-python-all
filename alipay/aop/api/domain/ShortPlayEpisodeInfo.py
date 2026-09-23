#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShortPlayEpisodeInfo(object):

    def __init__(self):
        self._cover = None
        self._file_id = None
        self._seq = None
        self._title = None

    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def seq(self):
        return self._seq

    @seq.setter
    def seq(self, value):
        self._seq = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.seq:
            if hasattr(self.seq, 'to_alipay_dict'):
                params['seq'] = self.seq.to_alipay_dict()
            else:
                params['seq'] = self.seq
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
        o = ShortPlayEpisodeInfo()
        if 'cover' in d:
            o.cover = d['cover']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'seq' in d:
            o.seq = d['seq']
        if 'title' in d:
            o.title = d['title']
        return o


