#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupAccountVO(object):

    def __init__(self):
        self._biz_entity_type = None
        self._collect_account_no = None
        self._scope_item = None

    @property
    def biz_entity_type(self):
        return self._biz_entity_type

    @biz_entity_type.setter
    def biz_entity_type(self, value):
        self._biz_entity_type = value
    @property
    def collect_account_no(self):
        return self._collect_account_no

    @collect_account_no.setter
    def collect_account_no(self, value):
        self._collect_account_no = value
    @property
    def scope_item(self):
        return self._scope_item

    @scope_item.setter
    def scope_item(self, value):
        self._scope_item = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_entity_type:
            if hasattr(self.biz_entity_type, 'to_alipay_dict'):
                params['biz_entity_type'] = self.biz_entity_type.to_alipay_dict()
            else:
                params['biz_entity_type'] = self.biz_entity_type
        if self.collect_account_no:
            if hasattr(self.collect_account_no, 'to_alipay_dict'):
                params['collect_account_no'] = self.collect_account_no.to_alipay_dict()
            else:
                params['collect_account_no'] = self.collect_account_no
        if self.scope_item:
            if hasattr(self.scope_item, 'to_alipay_dict'):
                params['scope_item'] = self.scope_item.to_alipay_dict()
            else:
                params['scope_item'] = self.scope_item
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupAccountVO()
        if 'biz_entity_type' in d:
            o.biz_entity_type = d['biz_entity_type']
        if 'collect_account_no' in d:
            o.collect_account_no = d['collect_account_no']
        if 'scope_item' in d:
            o.scope_item = d['scope_item']
        return o


