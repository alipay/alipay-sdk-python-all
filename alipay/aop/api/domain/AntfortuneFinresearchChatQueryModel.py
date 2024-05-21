#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchChatQueryModel(object):

    def __init__(self):
        self._bu_unique_id = None
        self._message_id = None
        self._session_id = None
        self._tenant_id = None

    @property
    def bu_unique_id(self):
        return self._bu_unique_id

    @bu_unique_id.setter
    def bu_unique_id(self, value):
        self._bu_unique_id = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bu_unique_id:
            if hasattr(self.bu_unique_id, 'to_alipay_dict'):
                params['bu_unique_id'] = self.bu_unique_id.to_alipay_dict()
            else:
                params['bu_unique_id'] = self.bu_unique_id
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchChatQueryModel()
        if 'bu_unique_id' in d:
            o.bu_unique_id = d['bu_unique_id']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


