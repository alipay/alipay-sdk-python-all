#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiMatterAttachmentDTO import OpenApiMatterAttachmentDTO


class OpenApiMatterCommentDTO(object):

    def __init__(self):
        self._attachment_list = None
        self._comment_code = None
        self._content = None
        self._gmt_create = None
        self._matter_code = None
        self._publisher_id = None
        self._publisher_name = None
        self._replied_comment_code = None
        self._replied_content = None

    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        if isinstance(value, list):
            self._attachment_list = list()
            for i in value:
                if isinstance(i, OpenApiMatterAttachmentDTO):
                    self._attachment_list.append(i)
                else:
                    self._attachment_list.append(OpenApiMatterAttachmentDTO.from_alipay_dict(i))
    @property
    def comment_code(self):
        return self._comment_code

    @comment_code.setter
    def comment_code(self, value):
        self._comment_code = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def matter_code(self):
        return self._matter_code

    @matter_code.setter
    def matter_code(self, value):
        self._matter_code = value
    @property
    def publisher_id(self):
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value):
        self._publisher_id = value
    @property
    def publisher_name(self):
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, value):
        self._publisher_name = value
    @property
    def replied_comment_code(self):
        return self._replied_comment_code

    @replied_comment_code.setter
    def replied_comment_code(self, value):
        self._replied_comment_code = value
    @property
    def replied_content(self):
        return self._replied_content

    @replied_content.setter
    def replied_content(self, value):
        self._replied_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_list:
            if isinstance(self.attachment_list, list):
                for i in range(0, len(self.attachment_list)):
                    element = self.attachment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_list[i] = element.to_alipay_dict()
            if hasattr(self.attachment_list, 'to_alipay_dict'):
                params['attachment_list'] = self.attachment_list.to_alipay_dict()
            else:
                params['attachment_list'] = self.attachment_list
        if self.comment_code:
            if hasattr(self.comment_code, 'to_alipay_dict'):
                params['comment_code'] = self.comment_code.to_alipay_dict()
            else:
                params['comment_code'] = self.comment_code
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.matter_code:
            if hasattr(self.matter_code, 'to_alipay_dict'):
                params['matter_code'] = self.matter_code.to_alipay_dict()
            else:
                params['matter_code'] = self.matter_code
        if self.publisher_id:
            if hasattr(self.publisher_id, 'to_alipay_dict'):
                params['publisher_id'] = self.publisher_id.to_alipay_dict()
            else:
                params['publisher_id'] = self.publisher_id
        if self.publisher_name:
            if hasattr(self.publisher_name, 'to_alipay_dict'):
                params['publisher_name'] = self.publisher_name.to_alipay_dict()
            else:
                params['publisher_name'] = self.publisher_name
        if self.replied_comment_code:
            if hasattr(self.replied_comment_code, 'to_alipay_dict'):
                params['replied_comment_code'] = self.replied_comment_code.to_alipay_dict()
            else:
                params['replied_comment_code'] = self.replied_comment_code
        if self.replied_content:
            if hasattr(self.replied_content, 'to_alipay_dict'):
                params['replied_content'] = self.replied_content.to_alipay_dict()
            else:
                params['replied_content'] = self.replied_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiMatterCommentDTO()
        if 'attachment_list' in d:
            o.attachment_list = d['attachment_list']
        if 'comment_code' in d:
            o.comment_code = d['comment_code']
        if 'content' in d:
            o.content = d['content']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'matter_code' in d:
            o.matter_code = d['matter_code']
        if 'publisher_id' in d:
            o.publisher_id = d['publisher_id']
        if 'publisher_name' in d:
            o.publisher_name = d['publisher_name']
        if 'replied_comment_code' in d:
            o.replied_comment_code = d['replied_comment_code']
        if 'replied_content' in d:
            o.replied_content = d['replied_content']
        return o


