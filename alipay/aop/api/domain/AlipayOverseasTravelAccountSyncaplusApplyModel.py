#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelAccountSyncaplusApplyModel(object):

    def __init__(self):
        self._aplus_owner_email = None
        self._aplus_owner_id = None
        self._aplus_owner_name = None
        self._cn_owner_id = None
        self._cn_owner_ids = None
        self._cn_trade_pid = None

    @property
    def aplus_owner_email(self):
        return self._aplus_owner_email

    @aplus_owner_email.setter
    def aplus_owner_email(self, value):
        self._aplus_owner_email = value
    @property
    def aplus_owner_id(self):
        return self._aplus_owner_id

    @aplus_owner_id.setter
    def aplus_owner_id(self, value):
        self._aplus_owner_id = value
    @property
    def aplus_owner_name(self):
        return self._aplus_owner_name

    @aplus_owner_name.setter
    def aplus_owner_name(self, value):
        self._aplus_owner_name = value
    @property
    def cn_owner_id(self):
        return self._cn_owner_id

    @cn_owner_id.setter
    def cn_owner_id(self, value):
        self._cn_owner_id = value
    @property
    def cn_owner_ids(self):
        return self._cn_owner_ids

    @cn_owner_ids.setter
    def cn_owner_ids(self, value):
        if isinstance(value, list):
            self._cn_owner_ids = list()
            for i in value:
                self._cn_owner_ids.append(i)
    @property
    def cn_trade_pid(self):
        return self._cn_trade_pid

    @cn_trade_pid.setter
    def cn_trade_pid(self, value):
        self._cn_trade_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.aplus_owner_email:
            if hasattr(self.aplus_owner_email, 'to_alipay_dict'):
                params['aplus_owner_email'] = self.aplus_owner_email.to_alipay_dict()
            else:
                params['aplus_owner_email'] = self.aplus_owner_email
        if self.aplus_owner_id:
            if hasattr(self.aplus_owner_id, 'to_alipay_dict'):
                params['aplus_owner_id'] = self.aplus_owner_id.to_alipay_dict()
            else:
                params['aplus_owner_id'] = self.aplus_owner_id
        if self.aplus_owner_name:
            if hasattr(self.aplus_owner_name, 'to_alipay_dict'):
                params['aplus_owner_name'] = self.aplus_owner_name.to_alipay_dict()
            else:
                params['aplus_owner_name'] = self.aplus_owner_name
        if self.cn_owner_id:
            if hasattr(self.cn_owner_id, 'to_alipay_dict'):
                params['cn_owner_id'] = self.cn_owner_id.to_alipay_dict()
            else:
                params['cn_owner_id'] = self.cn_owner_id
        if self.cn_owner_ids:
            if isinstance(self.cn_owner_ids, list):
                for i in range(0, len(self.cn_owner_ids)):
                    element = self.cn_owner_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cn_owner_ids[i] = element.to_alipay_dict()
            if hasattr(self.cn_owner_ids, 'to_alipay_dict'):
                params['cn_owner_ids'] = self.cn_owner_ids.to_alipay_dict()
            else:
                params['cn_owner_ids'] = self.cn_owner_ids
        if self.cn_trade_pid:
            if hasattr(self.cn_trade_pid, 'to_alipay_dict'):
                params['cn_trade_pid'] = self.cn_trade_pid.to_alipay_dict()
            else:
                params['cn_trade_pid'] = self.cn_trade_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelAccountSyncaplusApplyModel()
        if 'aplus_owner_email' in d:
            o.aplus_owner_email = d['aplus_owner_email']
        if 'aplus_owner_id' in d:
            o.aplus_owner_id = d['aplus_owner_id']
        if 'aplus_owner_name' in d:
            o.aplus_owner_name = d['aplus_owner_name']
        if 'cn_owner_id' in d:
            o.cn_owner_id = d['cn_owner_id']
        if 'cn_owner_ids' in d:
            o.cn_owner_ids = d['cn_owner_ids']
        if 'cn_trade_pid' in d:
            o.cn_trade_pid = d['cn_trade_pid']
        return o


