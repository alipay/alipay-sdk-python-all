#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfCommentSyncModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._comment_source = None
        self._comment_text = None
        self._commenter_name = None
        self._commenter_role = None
        self._out_comment_id = None
        self._out_live_id = None
        self._out_user_encode_id = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def comment_source(self):
        return self._comment_source

    @comment_source.setter
    def comment_source(self, value):
        self._comment_source = value
    @property
    def comment_text(self):
        return self._comment_text

    @comment_text.setter
    def comment_text(self, value):
        self._comment_text = value
    @property
    def commenter_name(self):
        return self._commenter_name

    @commenter_name.setter
    def commenter_name(self, value):
        self._commenter_name = value
    @property
    def commenter_role(self):
        return self._commenter_role

    @commenter_role.setter
    def commenter_role(self, value):
        self._commenter_role = value
    @property
    def out_comment_id(self):
        return self._out_comment_id

    @out_comment_id.setter
    def out_comment_id(self, value):
        self._out_comment_id = value
    @property
    def out_live_id(self):
        return self._out_live_id

    @out_live_id.setter
    def out_live_id(self, value):
        self._out_live_id = value
    @property
    def out_user_encode_id(self):
        return self._out_user_encode_id

    @out_user_encode_id.setter
    def out_user_encode_id(self, value):
        self._out_user_encode_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.comment_source:
            if hasattr(self.comment_source, 'to_alipay_dict'):
                params['comment_source'] = self.comment_source.to_alipay_dict()
            else:
                params['comment_source'] = self.comment_source
        if self.comment_text:
            if hasattr(self.comment_text, 'to_alipay_dict'):
                params['comment_text'] = self.comment_text.to_alipay_dict()
            else:
                params['comment_text'] = self.comment_text
        if self.commenter_name:
            if hasattr(self.commenter_name, 'to_alipay_dict'):
                params['commenter_name'] = self.commenter_name.to_alipay_dict()
            else:
                params['commenter_name'] = self.commenter_name
        if self.commenter_role:
            if hasattr(self.commenter_role, 'to_alipay_dict'):
                params['commenter_role'] = self.commenter_role.to_alipay_dict()
            else:
                params['commenter_role'] = self.commenter_role
        if self.out_comment_id:
            if hasattr(self.out_comment_id, 'to_alipay_dict'):
                params['out_comment_id'] = self.out_comment_id.to_alipay_dict()
            else:
                params['out_comment_id'] = self.out_comment_id
        if self.out_live_id:
            if hasattr(self.out_live_id, 'to_alipay_dict'):
                params['out_live_id'] = self.out_live_id.to_alipay_dict()
            else:
                params['out_live_id'] = self.out_live_id
        if self.out_user_encode_id:
            if hasattr(self.out_user_encode_id, 'to_alipay_dict'):
                params['out_user_encode_id'] = self.out_user_encode_id.to_alipay_dict()
            else:
                params['out_user_encode_id'] = self.out_user_encode_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfCommentSyncModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'comment_source' in d:
            o.comment_source = d['comment_source']
        if 'comment_text' in d:
            o.comment_text = d['comment_text']
        if 'commenter_name' in d:
            o.commenter_name = d['commenter_name']
        if 'commenter_role' in d:
            o.commenter_role = d['commenter_role']
        if 'out_comment_id' in d:
            o.out_comment_id = d['out_comment_id']
        if 'out_live_id' in d:
            o.out_live_id = d['out_live_id']
        if 'out_user_encode_id' in d:
            o.out_user_encode_id = d['out_user_encode_id']
        return o


