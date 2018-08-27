#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalSvTpCardBodyInfo(object):

    def __init__(self):
        self._content = None
        self._image_url = None
        self._link_url = None
        self._remark = None
        self._sub_contenet = None
        self._sub_title = None
        self._title = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sub_contenet(self):
        return self._sub_contenet

    @sub_contenet.setter
    def sub_contenet(self, value):
        self._sub_contenet = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sub_contenet:
            if hasattr(self.sub_contenet, 'to_alipay_dict'):
                params['sub_contenet'] = self.sub_contenet.to_alipay_dict()
            else:
                params['sub_contenet'] = self.sub_contenet
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalSvTpCardBodyInfo()
        if 'content' in d:
            o.content = d['content']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'remark' in d:
            o.remark = d['remark']
        if 'sub_contenet' in d:
            o.sub_contenet = d['sub_contenet']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


