#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemGwDTO import ItemGwDTO


class AlipayIserviceCcmSwItemSyncModel(object):

    def __init__(self):
        self._library_id = None
        self._lists = None
        self._syn_id = None

    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def lists(self):
        return self._lists

    @lists.setter
    def lists(self, value):
        if isinstance(value, ItemGwDTO):
            self._lists = value
        else:
            self._lists = ItemGwDTO.from_alipay_dict(value)
    @property
    def syn_id(self):
        return self._syn_id

    @syn_id.setter
    def syn_id(self, value):
        self._syn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
        if self.lists:
            if hasattr(self.lists, 'to_alipay_dict'):
                params['lists'] = self.lists.to_alipay_dict()
            else:
                params['lists'] = self.lists
        if self.syn_id:
            if hasattr(self.syn_id, 'to_alipay_dict'):
                params['syn_id'] = self.syn_id.to_alipay_dict()
            else:
                params['syn_id'] = self.syn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwItemSyncModel()
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'lists' in d:
            o.lists = d['lists']
        if 'syn_id' in d:
            o.syn_id = d['syn_id']
        return o


