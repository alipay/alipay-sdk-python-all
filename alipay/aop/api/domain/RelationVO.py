#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RelationVO(object):

    def __init__(self):
        self._oppo_account_name = None
        self._oppo_child_id = None
        self._oppo_head_url = None
        self._oppo_nick_name = None
        self._oppo_real_name = None

    @property
    def oppo_account_name(self):
        return self._oppo_account_name

    @oppo_account_name.setter
    def oppo_account_name(self, value):
        self._oppo_account_name = value
    @property
    def oppo_child_id(self):
        return self._oppo_child_id

    @oppo_child_id.setter
    def oppo_child_id(self, value):
        self._oppo_child_id = value
    @property
    def oppo_head_url(self):
        return self._oppo_head_url

    @oppo_head_url.setter
    def oppo_head_url(self, value):
        self._oppo_head_url = value
    @property
    def oppo_nick_name(self):
        return self._oppo_nick_name

    @oppo_nick_name.setter
    def oppo_nick_name(self, value):
        self._oppo_nick_name = value
    @property
    def oppo_real_name(self):
        return self._oppo_real_name

    @oppo_real_name.setter
    def oppo_real_name(self, value):
        self._oppo_real_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.oppo_account_name:
            if hasattr(self.oppo_account_name, 'to_alipay_dict'):
                params['oppo_account_name'] = self.oppo_account_name.to_alipay_dict()
            else:
                params['oppo_account_name'] = self.oppo_account_name
        if self.oppo_child_id:
            if hasattr(self.oppo_child_id, 'to_alipay_dict'):
                params['oppo_child_id'] = self.oppo_child_id.to_alipay_dict()
            else:
                params['oppo_child_id'] = self.oppo_child_id
        if self.oppo_head_url:
            if hasattr(self.oppo_head_url, 'to_alipay_dict'):
                params['oppo_head_url'] = self.oppo_head_url.to_alipay_dict()
            else:
                params['oppo_head_url'] = self.oppo_head_url
        if self.oppo_nick_name:
            if hasattr(self.oppo_nick_name, 'to_alipay_dict'):
                params['oppo_nick_name'] = self.oppo_nick_name.to_alipay_dict()
            else:
                params['oppo_nick_name'] = self.oppo_nick_name
        if self.oppo_real_name:
            if hasattr(self.oppo_real_name, 'to_alipay_dict'):
                params['oppo_real_name'] = self.oppo_real_name.to_alipay_dict()
            else:
                params['oppo_real_name'] = self.oppo_real_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RelationVO()
        if 'oppo_account_name' in d:
            o.oppo_account_name = d['oppo_account_name']
        if 'oppo_child_id' in d:
            o.oppo_child_id = d['oppo_child_id']
        if 'oppo_head_url' in d:
            o.oppo_head_url = d['oppo_head_url']
        if 'oppo_nick_name' in d:
            o.oppo_nick_name = d['oppo_nick_name']
        if 'oppo_real_name' in d:
            o.oppo_real_name = d['oppo_real_name']
        return o


