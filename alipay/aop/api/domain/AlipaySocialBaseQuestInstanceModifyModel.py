#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseQuestInstanceModifyModel(object):

    def __init__(self):
        self._quest_id = None
        self._remind_time_range = None
        self._source_id = None
        self._type = None
        self._user_id = None

    @property
    def quest_id(self):
        return self._quest_id

    @quest_id.setter
    def quest_id(self, value):
        self._quest_id = value
    @property
    def remind_time_range(self):
        return self._remind_time_range

    @remind_time_range.setter
    def remind_time_range(self, value):
        self._remind_time_range = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.quest_id:
            if hasattr(self.quest_id, 'to_alipay_dict'):
                params['quest_id'] = self.quest_id.to_alipay_dict()
            else:
                params['quest_id'] = self.quest_id
        if self.remind_time_range:
            if hasattr(self.remind_time_range, 'to_alipay_dict'):
                params['remind_time_range'] = self.remind_time_range.to_alipay_dict()
            else:
                params['remind_time_range'] = self.remind_time_range
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseQuestInstanceModifyModel()
        if 'quest_id' in d:
            o.quest_id = d['quest_id']
        if 'remind_time_range' in d:
            o.remind_time_range = d['remind_time_range']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


