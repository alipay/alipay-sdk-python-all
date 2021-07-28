#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainPoolSignadvanceSyncModel(object):

    def __init__(self):
        self._alipay_id = None
        self._channel_tag = None
        self._data_org_ip_role_id = None
        self._operate_category = None
        self._operate_type = None
        self._reject_msg = None

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
    @property
    def operate_category(self):
        return self._operate_category

    @operate_category.setter
    def operate_category(self, value):
        self._operate_category = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def reject_msg(self):
        return self._reject_msg

    @reject_msg.setter
    def reject_msg(self, value):
        self._reject_msg = value


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
        if self.operate_category:
            if hasattr(self.operate_category, 'to_alipay_dict'):
                params['operate_category'] = self.operate_category.to_alipay_dict()
            else:
                params['operate_category'] = self.operate_category
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.reject_msg:
            if hasattr(self.reject_msg, 'to_alipay_dict'):
                params['reject_msg'] = self.reject_msg.to_alipay_dict()
            else:
                params['reject_msg'] = self.reject_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainPoolSignadvanceSyncModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'channel_tag' in d:
            o.channel_tag = d['channel_tag']
        if 'data_org_ip_role_id' in d:
            o.data_org_ip_role_id = d['data_org_ip_role_id']
        if 'operate_category' in d:
            o.operate_category = d['operate_category']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'reject_msg' in d:
            o.reject_msg = d['reject_msg']
        return o


