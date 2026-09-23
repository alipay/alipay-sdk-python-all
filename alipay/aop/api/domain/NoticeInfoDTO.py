#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NoticeInfoDTO(object):

    def __init__(self):
        self._notice_content = None
        self._notice_pic_url = None
        self._title = None

    @property
    def notice_content(self):
        return self._notice_content

    @notice_content.setter
    def notice_content(self, value):
        self._notice_content = value
    @property
    def notice_pic_url(self):
        return self._notice_pic_url

    @notice_pic_url.setter
    def notice_pic_url(self, value):
        self._notice_pic_url = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.notice_content:
            if hasattr(self.notice_content, 'to_alipay_dict'):
                params['notice_content'] = self.notice_content.to_alipay_dict()
            else:
                params['notice_content'] = self.notice_content
        if self.notice_pic_url:
            if hasattr(self.notice_pic_url, 'to_alipay_dict'):
                params['notice_pic_url'] = self.notice_pic_url.to_alipay_dict()
            else:
                params['notice_pic_url'] = self.notice_pic_url
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
        o = NoticeInfoDTO()
        if 'notice_content' in d:
            o.notice_content = d['notice_content']
        if 'notice_pic_url' in d:
            o.notice_pic_url = d['notice_pic_url']
        if 'title' in d:
            o.title = d['title']
        return o


