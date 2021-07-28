#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneLifemssageSingleSendModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._public_id = None
        self._push_context = None
        self._template_context = None
        self._template_id = None
        self._to_user_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def push_context(self):
        return self._push_context

    @push_context.setter
    def push_context(self, value):
        self._push_context = value
    @property
    def template_context(self):
        return self._template_context

    @template_context.setter
    def template_context(self, value):
        self._template_context = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.push_context:
            if hasattr(self.push_context, 'to_alipay_dict'):
                params['push_context'] = self.push_context.to_alipay_dict()
            else:
                params['push_context'] = self.push_context
        if self.template_context:
            if hasattr(self.template_context, 'to_alipay_dict'):
                params['template_context'] = self.template_context.to_alipay_dict()
            else:
                params['template_context'] = self.template_context
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.to_user_id:
            if hasattr(self.to_user_id, 'to_alipay_dict'):
                params['to_user_id'] = self.to_user_id.to_alipay_dict()
            else:
                params['to_user_id'] = self.to_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneLifemssageSingleSendModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'push_context' in d:
            o.push_context = d['push_context']
        if 'template_context' in d:
            o.template_context = d['template_context']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


