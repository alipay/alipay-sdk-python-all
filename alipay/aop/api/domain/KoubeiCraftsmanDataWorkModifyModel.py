#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCraftsmanDataWorkModifyModel(object):

    def __init__(self):
        self._auth_code = None
        self._title = None
        self._work_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCraftsmanDataWorkModifyModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'title' in d:
            o.title = d['title']
        if 'work_id' in d:
            o.work_id = d['work_id']
        return o


