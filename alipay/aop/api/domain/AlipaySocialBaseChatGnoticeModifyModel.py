#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseChatGnoticeModifyModel(object):

    def __init__(self):
        self._group_id = None
        self._group_notice = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_notice(self):
        return self._group_notice

    @group_notice.setter
    def group_notice(self, value):
        self._group_notice = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_notice:
            if hasattr(self.group_notice, 'to_alipay_dict'):
                params['group_notice'] = self.group_notice.to_alipay_dict()
            else:
                params['group_notice'] = self.group_notice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseChatGnoticeModifyModel()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_notice' in d:
            o.group_notice = d['group_notice']
        return o


