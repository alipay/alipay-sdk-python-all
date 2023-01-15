#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseQuestInstancesQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._quest_ids = None
        self._source_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def quest_ids(self):
        return self._quest_ids

    @quest_ids.setter
    def quest_ids(self, value):
        if isinstance(value, list):
            self._quest_ids = list()
            for i in value:
                self._quest_ids.append(i)
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.quest_ids:
            if isinstance(self.quest_ids, list):
                for i in range(0, len(self.quest_ids)):
                    element = self.quest_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quest_ids[i] = element.to_alipay_dict()
            if hasattr(self.quest_ids, 'to_alipay_dict'):
                params['quest_ids'] = self.quest_ids.to_alipay_dict()
            else:
                params['quest_ids'] = self.quest_ids
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
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
        o = AlipaySocialBaseQuestInstancesQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'quest_ids' in d:
            o.quest_ids = d['quest_ids']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


