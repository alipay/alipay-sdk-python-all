#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseChatGinvSendModel(object):

    def __init__(self):
        self._group_id = None
        self._uids = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def uids(self):
        return self._uids

    @uids.setter
    def uids(self, value):
        if isinstance(value, list):
            self._uids = list()
            for i in value:
                self._uids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.uids:
            if isinstance(self.uids, list):
                for i in range(0, len(self.uids)):
                    element = self.uids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uids[i] = element.to_alipay_dict()
            if hasattr(self.uids, 'to_alipay_dict'):
                params['uids'] = self.uids.to_alipay_dict()
            else:
                params['uids'] = self.uids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseChatGinvSendModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'uids' in d:
            o.uids = d['uids']
        return o


