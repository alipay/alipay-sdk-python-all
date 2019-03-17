#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrincipalForOpenapi import PrincipalForOpenapi
from alipay.aop.api.domain.ContentObjectRelationForOpenapi import ContentObjectRelationForOpenapi
from alipay.aop.api.domain.ContentExtensionForOpenapi import ContentExtensionForOpenapi
from alipay.aop.api.domain.LabelForOpenapi import LabelForOpenapi


class KoubeiContentContentinfoCreateModel(object):

    def __init__(self):
        self._action_url = None
        self._author = None
        self._biz_type = None
        self._content_desc = None
        self._content_object_relation_list = None
        self._content_type = None
        self._cover_pics = None
        self._ext_into = None
        self._extensions = None
        self._external_id = None
        self._label_list = None
        self._request_token = None
        self._status = None
        self._sub_title = None
        self._title = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, PrincipalForOpenapi):
            self._author = value
        else:
            self._author = PrincipalForOpenapi.from_alipay_dict(value)
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def content_desc(self):
        return self._content_desc

    @content_desc.setter
    def content_desc(self, value):
        self._content_desc = value
    @property
    def content_object_relation_list(self):
        return self._content_object_relation_list

    @content_object_relation_list.setter
    def content_object_relation_list(self, value):
        if isinstance(value, list):
            self._content_object_relation_list = list()
            for i in value:
                if isinstance(i, ContentObjectRelationForOpenapi):
                    self._content_object_relation_list.append(i)
                else:
                    self._content_object_relation_list.append(ContentObjectRelationForOpenapi.from_alipay_dict(i))
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def cover_pics(self):
        return self._cover_pics

    @cover_pics.setter
    def cover_pics(self, value):
        if isinstance(value, list):
            self._cover_pics = list()
            for i in value:
                self._cover_pics.append(i)
    @property
    def ext_into(self):
        return self._ext_into

    @ext_into.setter
    def ext_into(self, value):
        self._ext_into = value
    @property
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, value):
        if isinstance(value, list):
            self._extensions = list()
            for i in value:
                if isinstance(i, ContentExtensionForOpenapi):
                    self._extensions.append(i)
                else:
                    self._extensions.append(ContentExtensionForOpenapi.from_alipay_dict(i))
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def label_list(self):
        return self._label_list

    @label_list.setter
    def label_list(self, value):
        if isinstance(value, list):
            self._label_list = list()
            for i in value:
                if isinstance(i, LabelForOpenapi):
                    self._label_list.append(i)
                else:
                    self._label_list.append(LabelForOpenapi.from_alipay_dict(i))
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.content_desc:
            if hasattr(self.content_desc, 'to_alipay_dict'):
                params['content_desc'] = self.content_desc.to_alipay_dict()
            else:
                params['content_desc'] = self.content_desc
        if self.content_object_relation_list:
            if isinstance(self.content_object_relation_list, list):
                for i in range(0, len(self.content_object_relation_list)):
                    element = self.content_object_relation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_object_relation_list[i] = element.to_alipay_dict()
            if hasattr(self.content_object_relation_list, 'to_alipay_dict'):
                params['content_object_relation_list'] = self.content_object_relation_list.to_alipay_dict()
            else:
                params['content_object_relation_list'] = self.content_object_relation_list
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.cover_pics:
            if isinstance(self.cover_pics, list):
                for i in range(0, len(self.cover_pics)):
                    element = self.cover_pics[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cover_pics[i] = element.to_alipay_dict()
            if hasattr(self.cover_pics, 'to_alipay_dict'):
                params['cover_pics'] = self.cover_pics.to_alipay_dict()
            else:
                params['cover_pics'] = self.cover_pics
        if self.ext_into:
            if hasattr(self.ext_into, 'to_alipay_dict'):
                params['ext_into'] = self.ext_into.to_alipay_dict()
            else:
                params['ext_into'] = self.ext_into
        if self.extensions:
            if isinstance(self.extensions, list):
                for i in range(0, len(self.extensions)):
                    element = self.extensions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extensions[i] = element.to_alipay_dict()
            if hasattr(self.extensions, 'to_alipay_dict'):
                params['extensions'] = self.extensions.to_alipay_dict()
            else:
                params['extensions'] = self.extensions
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.label_list:
            if isinstance(self.label_list, list):
                for i in range(0, len(self.label_list)):
                    element = self.label_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_list[i] = element.to_alipay_dict()
            if hasattr(self.label_list, 'to_alipay_dict'):
                params['label_list'] = self.label_list.to_alipay_dict()
            else:
                params['label_list'] = self.label_list
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = KoubeiContentContentinfoCreateModel()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'author' in d:
            o.author = d['author']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'content_desc' in d:
            o.content_desc = d['content_desc']
        if 'content_object_relation_list' in d:
            o.content_object_relation_list = d['content_object_relation_list']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'cover_pics' in d:
            o.cover_pics = d['cover_pics']
        if 'ext_into' in d:
            o.ext_into = d['ext_into']
        if 'extensions' in d:
            o.extensions = d['extensions']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'label_list' in d:
            o.label_list = d['label_list']
        if 'request_token' in d:
            o.request_token = d['request_token']
        if 'status' in d:
            o.status = d['status']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        return o


