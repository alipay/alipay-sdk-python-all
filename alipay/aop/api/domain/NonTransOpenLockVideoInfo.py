#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NonTransOpenLockVideoInfo(object):

    def __init__(self):
        self._fail_reason = None
        self._video_id = None
        self._video_urls = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value
    @property
    def video_urls(self):
        return self._video_urls

    @video_urls.setter
    def video_urls(self, value):
        if isinstance(value, list):
            self._video_urls = list()
            for i in value:
                self._video_urls.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.video_id:
            if hasattr(self.video_id, 'to_alipay_dict'):
                params['video_id'] = self.video_id.to_alipay_dict()
            else:
                params['video_id'] = self.video_id
        if self.video_urls:
            if isinstance(self.video_urls, list):
                for i in range(0, len(self.video_urls)):
                    element = self.video_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_urls[i] = element.to_alipay_dict()
            if hasattr(self.video_urls, 'to_alipay_dict'):
                params['video_urls'] = self.video_urls.to_alipay_dict()
            else:
                params['video_urls'] = self.video_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NonTransOpenLockVideoInfo()
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'video_urls' in d:
            o.video_urls = d['video_urls']
        return o


