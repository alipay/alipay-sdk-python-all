#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AliveSubtitleExt import AliveSubtitleExt


class AntfortuneContentCommunitySubtitleQueryModel(object):

    def __init__(self):
        self._content = None
        self._ext = None
        self._live_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        if isinstance(value, AliveSubtitleExt):
            self._ext = value
        else:
            self._ext = AliveSubtitleExt.from_alipay_dict(value)
    @property
    def live_id(self):
        return self._live_id

    @live_id.setter
    def live_id(self, value):
        self._live_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.live_id:
            if hasattr(self.live_id, 'to_alipay_dict'):
                params['live_id'] = self.live_id.to_alipay_dict()
            else:
                params['live_id'] = self.live_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneContentCommunitySubtitleQueryModel()
        if 'content' in d:
            o.content = d['content']
        if 'ext' in d:
            o.ext = d['ext']
        if 'live_id' in d:
            o.live_id = d['live_id']
        return o


