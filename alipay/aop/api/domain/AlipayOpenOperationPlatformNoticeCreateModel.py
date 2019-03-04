#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationPlatformNoticeCreateModel(object):

    def __init__(self):
        self._notice_content = None
        self._notice_title = None
        self._pid = None

    @property
    def notice_content(self):
        return self._notice_content

    @notice_content.setter
    def notice_content(self, value):
        self._notice_content = value
    @property
    def notice_title(self):
        return self._notice_title

    @notice_title.setter
    def notice_title(self, value):
        self._notice_title = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.notice_content:
            if hasattr(self.notice_content, 'to_alipay_dict'):
                params['notice_content'] = self.notice_content.to_alipay_dict()
            else:
                params['notice_content'] = self.notice_content
        if self.notice_title:
            if hasattr(self.notice_title, 'to_alipay_dict'):
                params['notice_title'] = self.notice_title.to_alipay_dict()
            else:
                params['notice_title'] = self.notice_title
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationPlatformNoticeCreateModel()
        if 'notice_content' in d:
            o.notice_content = d['notice_content']
        if 'notice_title' in d:
            o.notice_title = d['notice_title']
        if 'pid' in d:
            o.pid = d['pid']
        return o


