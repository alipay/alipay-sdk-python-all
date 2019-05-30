#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentOrganization(object):

    def __init__(self):
        self._agent_merchant_id = None
        self._cid = None
        self._cid_name = None

    @property
    def agent_merchant_id(self):
        return self._agent_merchant_id

    @agent_merchant_id.setter
    def agent_merchant_id(self, value):
        self._agent_merchant_id = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def cid_name(self):
        return self._cid_name

    @cid_name.setter
    def cid_name(self, value):
        self._cid_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_merchant_id:
            if hasattr(self.agent_merchant_id, 'to_alipay_dict'):
                params['agent_merchant_id'] = self.agent_merchant_id.to_alipay_dict()
            else:
                params['agent_merchant_id'] = self.agent_merchant_id
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.cid_name:
            if hasattr(self.cid_name, 'to_alipay_dict'):
                params['cid_name'] = self.cid_name.to_alipay_dict()
            else:
                params['cid_name'] = self.cid_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentOrganization()
        if 'agent_merchant_id' in d:
            o.agent_merchant_id = d['agent_merchant_id']
        if 'cid' in d:
            o.cid = d['cid']
        if 'cid_name' in d:
            o.cid_name = d['cid_name']
        return o


