#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultantInterpretVO(object):

    def __init__(self):
        self._content_md = None
        self._create_time = None
        self._finish_time = None
        self._interp_biz_id = None
        self._status = None
        self._summary = None
        self._title = None

    @property
    def content_md(self):
        return self._content_md

    @content_md.setter
    def content_md(self, value):
        self._content_md = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def interp_biz_id(self):
        return self._interp_biz_id

    @interp_biz_id.setter
    def interp_biz_id(self, value):
        self._interp_biz_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_md:
            if hasattr(self.content_md, 'to_alipay_dict'):
                params['content_md'] = self.content_md.to_alipay_dict()
            else:
                params['content_md'] = self.content_md
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.interp_biz_id:
            if hasattr(self.interp_biz_id, 'to_alipay_dict'):
                params['interp_biz_id'] = self.interp_biz_id.to_alipay_dict()
            else:
                params['interp_biz_id'] = self.interp_biz_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
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
        o = ConsultantInterpretVO()
        if 'content_md' in d:
            o.content_md = d['content_md']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'interp_biz_id' in d:
            o.interp_biz_id = d['interp_biz_id']
        if 'status' in d:
            o.status = d['status']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        return o


