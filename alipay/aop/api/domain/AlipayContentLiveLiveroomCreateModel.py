#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveLiveroomCreateModel(object):

    def __init__(self):
        self._alipay_advance_id = None
        self._alipay_public_id = None
        self._cover_url = None
        self._cover_url_3_x_4 = None
        self._live_biz_scene = None
        self._live_stream_url = None
        self._live_title = None
        self._out_live_id = None

    @property
    def alipay_advance_id(self):
        return self._alipay_advance_id

    @alipay_advance_id.setter
    def alipay_advance_id(self, value):
        self._alipay_advance_id = value
    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def cover_url(self):
        return self._cover_url

    @cover_url.setter
    def cover_url(self, value):
        self._cover_url = value
    @property
    def cover_url_3_x_4(self):
        return self._cover_url_3_x_4

    @cover_url_3_x_4.setter
    def cover_url_3_x_4(self, value):
        self._cover_url_3_x_4 = value
    @property
    def live_biz_scene(self):
        return self._live_biz_scene

    @live_biz_scene.setter
    def live_biz_scene(self, value):
        self._live_biz_scene = value
    @property
    def live_stream_url(self):
        return self._live_stream_url

    @live_stream_url.setter
    def live_stream_url(self, value):
        self._live_stream_url = value
    @property
    def live_title(self):
        return self._live_title

    @live_title.setter
    def live_title(self, value):
        self._live_title = value
    @property
    def out_live_id(self):
        return self._out_live_id

    @out_live_id.setter
    def out_live_id(self, value):
        self._out_live_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_advance_id:
            if hasattr(self.alipay_advance_id, 'to_alipay_dict'):
                params['alipay_advance_id'] = self.alipay_advance_id.to_alipay_dict()
            else:
                params['alipay_advance_id'] = self.alipay_advance_id
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.cover_url:
            if hasattr(self.cover_url, 'to_alipay_dict'):
                params['cover_url'] = self.cover_url.to_alipay_dict()
            else:
                params['cover_url'] = self.cover_url
        if self.cover_url_3_x_4:
            if hasattr(self.cover_url_3_x_4, 'to_alipay_dict'):
                params['cover_url_3_x_4'] = self.cover_url_3_x_4.to_alipay_dict()
            else:
                params['cover_url_3_x_4'] = self.cover_url_3_x_4
        if self.live_biz_scene:
            if hasattr(self.live_biz_scene, 'to_alipay_dict'):
                params['live_biz_scene'] = self.live_biz_scene.to_alipay_dict()
            else:
                params['live_biz_scene'] = self.live_biz_scene
        if self.live_stream_url:
            if hasattr(self.live_stream_url, 'to_alipay_dict'):
                params['live_stream_url'] = self.live_stream_url.to_alipay_dict()
            else:
                params['live_stream_url'] = self.live_stream_url
        if self.live_title:
            if hasattr(self.live_title, 'to_alipay_dict'):
                params['live_title'] = self.live_title.to_alipay_dict()
            else:
                params['live_title'] = self.live_title
        if self.out_live_id:
            if hasattr(self.out_live_id, 'to_alipay_dict'):
                params['out_live_id'] = self.out_live_id.to_alipay_dict()
            else:
                params['out_live_id'] = self.out_live_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveLiveroomCreateModel()
        if 'alipay_advance_id' in d:
            o.alipay_advance_id = d['alipay_advance_id']
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'cover_url' in d:
            o.cover_url = d['cover_url']
        if 'cover_url_3_x_4' in d:
            o.cover_url_3_x_4 = d['cover_url_3_x_4']
        if 'live_biz_scene' in d:
            o.live_biz_scene = d['live_biz_scene']
        if 'live_stream_url' in d:
            o.live_stream_url = d['live_stream_url']
        if 'live_title' in d:
            o.live_title = d['live_title']
        if 'out_live_id' in d:
            o.out_live_id = d['out_live_id']
        return o


