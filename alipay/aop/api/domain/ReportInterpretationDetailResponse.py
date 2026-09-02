#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportInterpretationDetailResponse(object):

    def __init__(self):
        self._chat_id = None
        self._file_source = None
        self._file_type = None
        self._id = None
        self._interpretation_result = None
        self._open_id = None
        self._scene = None
        self._session_id = None
        self._user_id = None
        self._user_type = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def file_source(self):
        return self._file_source

    @file_source.setter
    def file_source(self, value):
        self._file_source = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def interpretation_result(self):
        return self._interpretation_result

    @interpretation_result.setter
    def interpretation_result(self, value):
        self._interpretation_result = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.file_source:
            if hasattr(self.file_source, 'to_alipay_dict'):
                params['file_source'] = self.file_source.to_alipay_dict()
            else:
                params['file_source'] = self.file_source
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.interpretation_result:
            if hasattr(self.interpretation_result, 'to_alipay_dict'):
                params['interpretation_result'] = self.interpretation_result.to_alipay_dict()
            else:
                params['interpretation_result'] = self.interpretation_result
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportInterpretationDetailResponse()
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'file_source' in d:
            o.file_source = d['file_source']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'id' in d:
            o.id = d['id']
        if 'interpretation_result' in d:
            o.interpretation_result = d['interpretation_result']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


