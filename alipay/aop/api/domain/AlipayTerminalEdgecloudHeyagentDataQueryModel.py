#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudHeyagentDataQueryModel(object):

    def __init__(self):
        self._agent_id = None
        self._data_type = None
        self._open_id = None
        self._uid = None
        self._utdid = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def utdid(self):
        return self._utdid

    @utdid.setter
    def utdid(self, value):
        self._utdid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.utdid:
            if hasattr(self.utdid, 'to_alipay_dict'):
                params['utdid'] = self.utdid.to_alipay_dict()
            else:
                params['utdid'] = self.utdid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudHeyagentDataQueryModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'uid' in d:
            o.uid = d['uid']
        if 'utdid' in d:
            o.utdid = d['utdid']
        return o


