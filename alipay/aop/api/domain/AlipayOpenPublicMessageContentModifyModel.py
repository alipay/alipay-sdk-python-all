#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicMessageContentModifyModel(object):

    def __init__(self):
        self._benefit = None
        self._content = None
        self._content_id = None
        self._could_comment = None
        self._cover = None
        self._ctype = None
        self._ext_tags = None
        self._login_ids = None
        self._title = None

    @property
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, value):
        self._benefit = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def could_comment(self):
        return self._could_comment

    @could_comment.setter
    def could_comment(self, value):
        self._could_comment = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def ctype(self):
        return self._ctype

    @ctype.setter
    def ctype(self, value):
        self._ctype = value
    @property
    def ext_tags(self):
        return self._ext_tags

    @ext_tags.setter
    def ext_tags(self, value):
        self._ext_tags = value
    @property
    def login_ids(self):
        return self._login_ids

    @login_ids.setter
    def login_ids(self, value):
        self._login_ids = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit:
            if hasattr(self.benefit, 'to_alipay_dict'):
                params['benefit'] = self.benefit.to_alipay_dict()
            else:
                params['benefit'] = self.benefit
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.could_comment:
            if hasattr(self.could_comment, 'to_alipay_dict'):
                params['could_comment'] = self.could_comment.to_alipay_dict()
            else:
                params['could_comment'] = self.could_comment
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.ctype:
            if hasattr(self.ctype, 'to_alipay_dict'):
                params['ctype'] = self.ctype.to_alipay_dict()
            else:
                params['ctype'] = self.ctype
        if self.ext_tags:
            if hasattr(self.ext_tags, 'to_alipay_dict'):
                params['ext_tags'] = self.ext_tags.to_alipay_dict()
            else:
                params['ext_tags'] = self.ext_tags
        if self.login_ids:
            if hasattr(self.login_ids, 'to_alipay_dict'):
                params['login_ids'] = self.login_ids.to_alipay_dict()
            else:
                params['login_ids'] = self.login_ids
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
        o = AlipayOpenPublicMessageContentModifyModel()
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'content' in d:
            o.content = d['content']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'could_comment' in d:
            o.could_comment = d['could_comment']
        if 'cover' in d:
            o.cover = d['cover']
        if 'ctype' in d:
            o.ctype = d['ctype']
        if 'ext_tags' in d:
            o.ext_tags = d['ext_tags']
        if 'login_ids' in d:
            o.login_ids = d['login_ids']
        if 'title' in d:
            o.title = d['title']
        return o


