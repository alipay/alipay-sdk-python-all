#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerifyResultInfo(object):

    def __init__(self):
        self._button_jump_url = None
        self._button_text = None
        self._main_title = None
        self._memo = None
        self._scene_code = None
        self._scene_desc = None
        self._status = None
        self._sub_title = None
        self._verify_issue_desc = None
        self._verify_issue_type = None

    @property
    def button_jump_url(self):
        return self._button_jump_url

    @button_jump_url.setter
    def button_jump_url(self, value):
        self._button_jump_url = value
    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_desc(self):
        return self._scene_desc

    @scene_desc.setter
    def scene_desc(self, value):
        self._scene_desc = value
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
    def verify_issue_desc(self):
        return self._verify_issue_desc

    @verify_issue_desc.setter
    def verify_issue_desc(self, value):
        self._verify_issue_desc = value
    @property
    def verify_issue_type(self):
        return self._verify_issue_type

    @verify_issue_type.setter
    def verify_issue_type(self, value):
        self._verify_issue_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.button_jump_url:
            if hasattr(self.button_jump_url, 'to_alipay_dict'):
                params['button_jump_url'] = self.button_jump_url.to_alipay_dict()
            else:
                params['button_jump_url'] = self.button_jump_url
        if self.button_text:
            if hasattr(self.button_text, 'to_alipay_dict'):
                params['button_text'] = self.button_text.to_alipay_dict()
            else:
                params['button_text'] = self.button_text
        if self.main_title:
            if hasattr(self.main_title, 'to_alipay_dict'):
                params['main_title'] = self.main_title.to_alipay_dict()
            else:
                params['main_title'] = self.main_title
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_desc:
            if hasattr(self.scene_desc, 'to_alipay_dict'):
                params['scene_desc'] = self.scene_desc.to_alipay_dict()
            else:
                params['scene_desc'] = self.scene_desc
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
        if self.verify_issue_desc:
            if hasattr(self.verify_issue_desc, 'to_alipay_dict'):
                params['verify_issue_desc'] = self.verify_issue_desc.to_alipay_dict()
            else:
                params['verify_issue_desc'] = self.verify_issue_desc
        if self.verify_issue_type:
            if hasattr(self.verify_issue_type, 'to_alipay_dict'):
                params['verify_issue_type'] = self.verify_issue_type.to_alipay_dict()
            else:
                params['verify_issue_type'] = self.verify_issue_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifyResultInfo()
        if 'button_jump_url' in d:
            o.button_jump_url = d['button_jump_url']
        if 'button_text' in d:
            o.button_text = d['button_text']
        if 'main_title' in d:
            o.main_title = d['main_title']
        if 'memo' in d:
            o.memo = d['memo']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_desc' in d:
            o.scene_desc = d['scene_desc']
        if 'status' in d:
            o.status = d['status']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'verify_issue_desc' in d:
            o.verify_issue_desc = d['verify_issue_desc']
        if 'verify_issue_type' in d:
            o.verify_issue_type = d['verify_issue_type']
        return o


