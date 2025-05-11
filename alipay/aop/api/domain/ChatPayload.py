#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileAttachment import FileAttachment


class ChatPayload(object):

    def __init__(self):
        self._attachments = None
        self._ctx_params = None
        self._query = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, FileAttachment):
                    self._attachments.append(i)
                else:
                    self._attachments.append(FileAttachment.from_alipay_dict(i))
    @property
    def ctx_params(self):
        return self._ctx_params

    @ctx_params.setter
    def ctx_params(self, value):
        self._ctx_params = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


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
        if self.ctx_params:
            if hasattr(self.ctx_params, 'to_alipay_dict'):
                params['ctx_params'] = self.ctx_params.to_alipay_dict()
            else:
                params['ctx_params'] = self.ctx_params
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatPayload()
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'ctx_params' in d:
            o.ctx_params = d['ctx_params']
        if 'query' in d:
            o.query = d['query']
        return o


