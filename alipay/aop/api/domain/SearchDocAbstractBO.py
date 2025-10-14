#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchDocAbstractBO(object):

    def __init__(self):
        self._abstract_offline = None
        self._abstract_online = None
        self._snippet = None

    @property
    def abstract_offline(self):
        return self._abstract_offline

    @abstract_offline.setter
    def abstract_offline(self, value):
        self._abstract_offline = value
    @property
    def abstract_online(self):
        return self._abstract_online

    @abstract_online.setter
    def abstract_online(self, value):
        self._abstract_online = value
    @property
    def snippet(self):
        return self._snippet

    @snippet.setter
    def snippet(self, value):
        self._snippet = value


    def to_alipay_dict(self):
        params = dict()
        if self.abstract_offline:
            if hasattr(self.abstract_offline, 'to_alipay_dict'):
                params['abstract_offline'] = self.abstract_offline.to_alipay_dict()
            else:
                params['abstract_offline'] = self.abstract_offline
        if self.abstract_online:
            if hasattr(self.abstract_online, 'to_alipay_dict'):
                params['abstract_online'] = self.abstract_online.to_alipay_dict()
            else:
                params['abstract_online'] = self.abstract_online
        if self.snippet:
            if hasattr(self.snippet, 'to_alipay_dict'):
                params['snippet'] = self.snippet.to_alipay_dict()
            else:
                params['snippet'] = self.snippet
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchDocAbstractBO()
        if 'abstract_offline' in d:
            o.abstract_offline = d['abstract_offline']
        if 'abstract_online' in d:
            o.abstract_online = d['abstract_online']
        if 'snippet' in d:
            o.snippet = d['snippet']
        return o


