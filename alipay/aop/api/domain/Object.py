#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Object(object):

    def __init__(self):
        self._doc_ids = None
        self._doc_media_type = None
        self._ids = None
        self._is_query_update_time = None
        self._levels = None
        self._page_now = None
        self._page_size = None
        self._project_ids = None
        self._status = None
        self._tag_ids = None
        self._type = None

    @property
    def doc_ids(self):
        return self._doc_ids

    @doc_ids.setter
    def doc_ids(self, value):
        if isinstance(value, list):
            self._doc_ids = list()
            for i in value:
                self._doc_ids.append(i)
    @property
    def doc_media_type(self):
        return self._doc_media_type

    @doc_media_type.setter
    def doc_media_type(self, value):
        if isinstance(value, list):
            self._doc_media_type = list()
            for i in value:
                self._doc_media_type.append(i)
    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)
    @property
    def is_query_update_time(self):
        return self._is_query_update_time

    @is_query_update_time.setter
    def is_query_update_time(self, value):
        self._is_query_update_time = value
    @property
    def levels(self):
        return self._levels

    @levels.setter
    def levels(self, value):
        if isinstance(value, list):
            self._levels = list()
            for i in value:
                self._levels.append(i)
    @property
    def page_now(self):
        return self._page_now

    @page_now.setter
    def page_now(self, value):
        self._page_now = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def project_ids(self):
        return self._project_ids

    @project_ids.setter
    def project_ids(self, value):
        if isinstance(value, list):
            self._project_ids = list()
            for i in value:
                self._project_ids.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def tag_ids(self):
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, value):
        if isinstance(value, list):
            self._tag_ids = list()
            for i in value:
                self._tag_ids.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.doc_ids:
            if isinstance(self.doc_ids, list):
                for i in range(0, len(self.doc_ids)):
                    element = self.doc_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doc_ids[i] = element.to_alipay_dict()
            if hasattr(self.doc_ids, 'to_alipay_dict'):
                params['doc_ids'] = self.doc_ids.to_alipay_dict()
            else:
                params['doc_ids'] = self.doc_ids
        if self.doc_media_type:
            if isinstance(self.doc_media_type, list):
                for i in range(0, len(self.doc_media_type)):
                    element = self.doc_media_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doc_media_type[i] = element.to_alipay_dict()
            if hasattr(self.doc_media_type, 'to_alipay_dict'):
                params['doc_media_type'] = self.doc_media_type.to_alipay_dict()
            else:
                params['doc_media_type'] = self.doc_media_type
        if self.ids:
            if isinstance(self.ids, list):
                for i in range(0, len(self.ids)):
                    element = self.ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ids[i] = element.to_alipay_dict()
            if hasattr(self.ids, 'to_alipay_dict'):
                params['ids'] = self.ids.to_alipay_dict()
            else:
                params['ids'] = self.ids
        if self.is_query_update_time:
            if hasattr(self.is_query_update_time, 'to_alipay_dict'):
                params['is_query_update_time'] = self.is_query_update_time.to_alipay_dict()
            else:
                params['is_query_update_time'] = self.is_query_update_time
        if self.levels:
            if isinstance(self.levels, list):
                for i in range(0, len(self.levels)):
                    element = self.levels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.levels[i] = element.to_alipay_dict()
            if hasattr(self.levels, 'to_alipay_dict'):
                params['levels'] = self.levels.to_alipay_dict()
            else:
                params['levels'] = self.levels
        if self.page_now:
            if hasattr(self.page_now, 'to_alipay_dict'):
                params['page_now'] = self.page_now.to_alipay_dict()
            else:
                params['page_now'] = self.page_now
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.project_ids:
            if isinstance(self.project_ids, list):
                for i in range(0, len(self.project_ids)):
                    element = self.project_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.project_ids[i] = element.to_alipay_dict()
            if hasattr(self.project_ids, 'to_alipay_dict'):
                params['project_ids'] = self.project_ids.to_alipay_dict()
            else:
                params['project_ids'] = self.project_ids
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tag_ids:
            if isinstance(self.tag_ids, list):
                for i in range(0, len(self.tag_ids)):
                    element = self.tag_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_ids[i] = element.to_alipay_dict()
            if hasattr(self.tag_ids, 'to_alipay_dict'):
                params['tag_ids'] = self.tag_ids.to_alipay_dict()
            else:
                params['tag_ids'] = self.tag_ids
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Object()
        if 'doc_ids' in d:
            o.doc_ids = d['doc_ids']
        if 'doc_media_type' in d:
            o.doc_media_type = d['doc_media_type']
        if 'ids' in d:
            o.ids = d['ids']
        if 'is_query_update_time' in d:
            o.is_query_update_time = d['is_query_update_time']
        if 'levels' in d:
            o.levels = d['levels']
        if 'page_now' in d:
            o.page_now = d['page_now']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'project_ids' in d:
            o.project_ids = d['project_ids']
        if 'status' in d:
            o.status = d['status']
        if 'tag_ids' in d:
            o.tag_ids = d['tag_ids']
        if 'type' in d:
            o.type = d['type']
        return o


