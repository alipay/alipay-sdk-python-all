#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGroupbuyingSyncModel(object):

    def __init__(self):
        self._group_expire = None
        self._group_id = None
        self._havana_id = None
        self._item_id = None

    @property
    def group_expire(self):
        return self._group_expire

    @group_expire.setter
    def group_expire(self, value):
        self._group_expire = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_expire:
            if hasattr(self.group_expire, 'to_alipay_dict'):
                params['group_expire'] = self.group_expire.to_alipay_dict()
            else:
                params['group_expire'] = self.group_expire
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGroupbuyingSyncModel()
        if 'group_expire' in d:
            o.group_expire = d['group_expire']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


