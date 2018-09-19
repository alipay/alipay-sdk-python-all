#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCraftsmanDataWorkDeleteModel(object):

    def __init__(self):
        self._auth_code = None
        self._craftsman_id = None
        self._work_ids = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value
    @property
    def work_ids(self):
        return self._work_ids

    @work_ids.setter
    def work_ids(self, value):
        if isinstance(value, list):
            self._work_ids = list()
            for i in value:
                self._work_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.craftsman_id:
            if hasattr(self.craftsman_id, 'to_alipay_dict'):
                params['craftsman_id'] = self.craftsman_id.to_alipay_dict()
            else:
                params['craftsman_id'] = self.craftsman_id
        if self.work_ids:
            if isinstance(self.work_ids, list):
                for i in range(0, len(self.work_ids)):
                    element = self.work_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_ids[i] = element.to_alipay_dict()
            if hasattr(self.work_ids, 'to_alipay_dict'):
                params['work_ids'] = self.work_ids.to_alipay_dict()
            else:
                params['work_ids'] = self.work_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCraftsmanDataWorkDeleteModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'craftsman_id' in d:
            o.craftsman_id = d['craftsman_id']
        if 'work_ids' in d:
            o.work_ids = d['work_ids']
        return o


