#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainPoolCreditsignadmitQueryModel(object):

    def __init__(self):
        self._alipay_id = None
        self._channel_tag = None
        self._data_org_ip_role_id = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def channel_tag(self):
        return self._channel_tag

    @channel_tag.setter
    def channel_tag(self, value):
        self._channel_tag = value
    @property
    def data_org_ip_role_id(self):
        return self._data_org_ip_role_id

    @data_org_ip_role_id.setter
    def data_org_ip_role_id(self, value):
        self._data_org_ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.channel_tag:
            if hasattr(self.channel_tag, 'to_alipay_dict'):
                params['channel_tag'] = self.channel_tag.to_alipay_dict()
            else:
                params['channel_tag'] = self.channel_tag
        if self.data_org_ip_role_id:
            if hasattr(self.data_org_ip_role_id, 'to_alipay_dict'):
                params['data_org_ip_role_id'] = self.data_org_ip_role_id.to_alipay_dict()
            else:
                params['data_org_ip_role_id'] = self.data_org_ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainPoolCreditsignadmitQueryModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'channel_tag' in d:
            o.channel_tag = d['channel_tag']
        if 'data_org_ip_role_id' in d:
            o.data_org_ip_role_id = d['data_org_ip_role_id']
        return o


