#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HistoryQueryAndAnswer import HistoryQueryAndAnswer


class AlipayEbppIndustryUserIntentionIdentifyModel(object):

    def __init__(self):
        self._history_list = None
        self._identity_id = None
        self._query = None
        self._session_id = None

    @property
    def history_list(self):
        return self._history_list

    @history_list.setter
    def history_list(self, value):
        if isinstance(value, list):
            self._history_list = list()
            for i in value:
                if isinstance(i, HistoryQueryAndAnswer):
                    self._history_list.append(i)
                else:
                    self._history_list.append(HistoryQueryAndAnswer.from_alipay_dict(i))
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.history_list:
            if isinstance(self.history_list, list):
                for i in range(0, len(self.history_list)):
                    element = self.history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.history_list[i] = element.to_alipay_dict()
            if hasattr(self.history_list, 'to_alipay_dict'):
                params['history_list'] = self.history_list.to_alipay_dict()
            else:
                params['history_list'] = self.history_list
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryUserIntentionIdentifyModel()
        if 'history_list' in d:
            o.history_list = d['history_list']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'query' in d:
            o.query = d['query']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


