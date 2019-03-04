#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentExtInfoModel import ContentExtInfoModel


class ContentInfoModel(object):

    def __init__(self):
        self._booth = None
        self._content_id_str = None
        self._ext_info = None
        self._link_url = None
        self._logo = None
        self._receive_status = None
        self._scene = None
        self._sub_title = None
        self._title = None
        self._touch_point = None

    @property
    def booth(self):
        return self._booth

    @booth.setter
    def booth(self, value):
        self._booth = value
    @property
    def content_id_str(self):
        return self._content_id_str

    @content_id_str.setter
    def content_id_str(self, value):
        self._content_id_str = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ContentExtInfoModel):
            self._ext_info = value
        else:
            self._ext_info = ContentExtInfoModel.from_alipay_dict(value)
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def receive_status(self):
        return self._receive_status

    @receive_status.setter
    def receive_status(self, value):
        self._receive_status = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def touch_point(self):
        return self._touch_point

    @touch_point.setter
    def touch_point(self, value):
        self._touch_point = value


    def to_alipay_dict(self):
        params = dict()
        if self.booth:
            if hasattr(self.booth, 'to_alipay_dict'):
                params['booth'] = self.booth.to_alipay_dict()
            else:
                params['booth'] = self.booth
        if self.content_id_str:
            if hasattr(self.content_id_str, 'to_alipay_dict'):
                params['content_id_str'] = self.content_id_str.to_alipay_dict()
            else:
                params['content_id_str'] = self.content_id_str
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.receive_status:
            if hasattr(self.receive_status, 'to_alipay_dict'):
                params['receive_status'] = self.receive_status.to_alipay_dict()
            else:
                params['receive_status'] = self.receive_status
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.touch_point:
            if hasattr(self.touch_point, 'to_alipay_dict'):
                params['touch_point'] = self.touch_point.to_alipay_dict()
            else:
                params['touch_point'] = self.touch_point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentInfoModel()
        if 'booth' in d:
            o.booth = d['booth']
        if 'content_id_str' in d:
            o.content_id_str = d['content_id_str']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'logo' in d:
            o.logo = d['logo']
        if 'receive_status' in d:
            o.receive_status = d['receive_status']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'touch_point' in d:
            o.touch_point = d['touch_point']
        return o


