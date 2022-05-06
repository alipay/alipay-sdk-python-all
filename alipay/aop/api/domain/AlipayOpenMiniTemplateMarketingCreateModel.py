#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniTemplateMarketingCreateModel(object):

    def __init__(self):
        self._activity_id = None
        self._gmt_end = None
        self._gmt_start = None
        self._template_ids = None
        self._title = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def template_ids(self):
        return self._template_ids

    @template_ids.setter
    def template_ids(self, value):
        if isinstance(value, list):
            self._template_ids = list()
            for i in value:
                self._template_ids.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.template_ids:
            if isinstance(self.template_ids, list):
                for i in range(0, len(self.template_ids)):
                    element = self.template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_ids[i] = element.to_alipay_dict()
            if hasattr(self.template_ids, 'to_alipay_dict'):
                params['template_ids'] = self.template_ids.to_alipay_dict()
            else:
                params['template_ids'] = self.template_ids
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
        o = AlipayOpenMiniTemplateMarketingCreateModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'template_ids' in d:
            o.template_ids = d['template_ids']
        if 'title' in d:
            o.title = d['title']
        return o


