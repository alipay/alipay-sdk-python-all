#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttachmentDetailInfo import AttachmentDetailInfo


class KnowledgeDetail(object):

    def __init__(self):
        self._attachments = None
        self._content = None
        self._knowledge_id = None
        self._library_id = None
        self._title = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, AttachmentDetailInfo):
                    self._attachments.append(i)
                else:
                    self._attachments.append(AttachmentDetailInfo.from_alipay_dict(i))
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def knowledge_id(self):
        return self._knowledge_id

    @knowledge_id.setter
    def knowledge_id(self, value):
        self._knowledge_id = value
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.knowledge_id:
            if hasattr(self.knowledge_id, 'to_alipay_dict'):
                params['knowledge_id'] = self.knowledge_id.to_alipay_dict()
            else:
                params['knowledge_id'] = self.knowledge_id
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
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
        o = KnowledgeDetail()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'content' in d:
            o.content = d['content']
        if 'knowledge_id' in d:
            o.knowledge_id = d['knowledge_id']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'title' in d:
            o.title = d['title']
        return o


