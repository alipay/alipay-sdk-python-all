#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GetAgentStatusVO(object):

    def __init__(self):
        self._ai_assistant_opened_status = None
        self._avatar_id = None
        self._legal_status = None
        self._redirect_url = None

    @property
    def ai_assistant_opened_status(self):
        return self._ai_assistant_opened_status

    @ai_assistant_opened_status.setter
    def ai_assistant_opened_status(self, value):
        self._ai_assistant_opened_status = value
    @property
    def avatar_id(self):
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, value):
        self._avatar_id = value
    @property
    def legal_status(self):
        return self._legal_status

    @legal_status.setter
    def legal_status(self, value):
        self._legal_status = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_assistant_opened_status:
            if hasattr(self.ai_assistant_opened_status, 'to_alipay_dict'):
                params['ai_assistant_opened_status'] = self.ai_assistant_opened_status.to_alipay_dict()
            else:
                params['ai_assistant_opened_status'] = self.ai_assistant_opened_status
        if self.avatar_id:
            if hasattr(self.avatar_id, 'to_alipay_dict'):
                params['avatar_id'] = self.avatar_id.to_alipay_dict()
            else:
                params['avatar_id'] = self.avatar_id
        if self.legal_status:
            if hasattr(self.legal_status, 'to_alipay_dict'):
                params['legal_status'] = self.legal_status.to_alipay_dict()
            else:
                params['legal_status'] = self.legal_status
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetAgentStatusVO()
        if 'ai_assistant_opened_status' in d:
            o.ai_assistant_opened_status = d['ai_assistant_opened_status']
        if 'avatar_id' in d:
            o.avatar_id = d['avatar_id']
        if 'legal_status' in d:
            o.legal_status = d['legal_status']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


