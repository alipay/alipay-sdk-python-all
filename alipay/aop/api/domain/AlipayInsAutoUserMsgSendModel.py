#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AutoMktTouchExtendInfoEntry import AutoMktTouchExtendInfoEntry
from alipay.aop.api.domain.AutoMktTouchExtendInfoEntry import AutoMktTouchExtendInfoEntry


class AlipayInsAutoUserMsgSendModel(object):

    def __init__(self):
        self._biz_time = None
        self._extend_info = None
        self._out_biz_no = None
        self._scene_code = None
        self._source = None
        self._template_content_info = None
        self._user_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        if isinstance(value, list):
            self._extend_info = list()
            for i in value:
                if isinstance(i, AutoMktTouchExtendInfoEntry):
                    self._extend_info.append(i)
                else:
                    self._extend_info.append(AutoMktTouchExtendInfoEntry.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def template_content_info(self):
        return self._template_content_info

    @template_content_info.setter
    def template_content_info(self, value):
        if isinstance(value, list):
            self._template_content_info = list()
            for i in value:
                if isinstance(i, AutoMktTouchExtendInfoEntry):
                    self._template_content_info.append(i)
                else:
                    self._template_content_info.append(AutoMktTouchExtendInfoEntry.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.extend_info:
            if isinstance(self.extend_info, list):
                for i in range(0, len(self.extend_info)):
                    element = self.extend_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_info[i] = element.to_alipay_dict()
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.template_content_info:
            if isinstance(self.template_content_info, list):
                for i in range(0, len(self.template_content_info)):
                    element = self.template_content_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_content_info[i] = element.to_alipay_dict()
            if hasattr(self.template_content_info, 'to_alipay_dict'):
                params['template_content_info'] = self.template_content_info.to_alipay_dict()
            else:
                params['template_content_info'] = self.template_content_info
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoUserMsgSendModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'source' in d:
            o.source = d['source']
        if 'template_content_info' in d:
            o.template_content_info = d['template_content_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


