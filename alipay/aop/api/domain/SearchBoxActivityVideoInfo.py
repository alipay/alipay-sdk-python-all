#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBoxActivityVideoInfo(object):

    def __init__(self):
        self._video_btn_text = None
        self._video_coverimg_id = None
        self._video_sub_title = None
        self._video_title = None

    @property
    def video_btn_text(self):
        return self._video_btn_text

    @video_btn_text.setter
    def video_btn_text(self, value):
        self._video_btn_text = value
    @property
    def video_coverimg_id(self):
        return self._video_coverimg_id

    @video_coverimg_id.setter
    def video_coverimg_id(self, value):
        self._video_coverimg_id = value
    @property
    def video_sub_title(self):
        return self._video_sub_title

    @video_sub_title.setter
    def video_sub_title(self, value):
        self._video_sub_title = value
    @property
    def video_title(self):
        return self._video_title

    @video_title.setter
    def video_title(self, value):
        self._video_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.video_btn_text:
            if hasattr(self.video_btn_text, 'to_alipay_dict'):
                params['video_btn_text'] = self.video_btn_text.to_alipay_dict()
            else:
                params['video_btn_text'] = self.video_btn_text
        if self.video_coverimg_id:
            if hasattr(self.video_coverimg_id, 'to_alipay_dict'):
                params['video_coverimg_id'] = self.video_coverimg_id.to_alipay_dict()
            else:
                params['video_coverimg_id'] = self.video_coverimg_id
        if self.video_sub_title:
            if hasattr(self.video_sub_title, 'to_alipay_dict'):
                params['video_sub_title'] = self.video_sub_title.to_alipay_dict()
            else:
                params['video_sub_title'] = self.video_sub_title
        if self.video_title:
            if hasattr(self.video_title, 'to_alipay_dict'):
                params['video_title'] = self.video_title.to_alipay_dict()
            else:
                params['video_title'] = self.video_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBoxActivityVideoInfo()
        if 'video_btn_text' in d:
            o.video_btn_text = d['video_btn_text']
        if 'video_coverimg_id' in d:
            o.video_coverimg_id = d['video_coverimg_id']
        if 'video_sub_title' in d:
            o.video_sub_title = d['video_sub_title']
        if 'video_title' in d:
            o.video_title = d['video_title']
        return o


