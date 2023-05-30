#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QipanMerchantCrowdUser import QipanMerchantCrowdUser


class AlipayMerchantQipanCrowdCreateModel(object):

    def __init__(self):
        self._apply_channel_list = None
        self._crowd_desc = None
        self._crowd_name = None
        self._external_crowd_code = None
        self._hidden = None
        self._user_list = None

    @property
    def apply_channel_list(self):
        return self._apply_channel_list

    @apply_channel_list.setter
    def apply_channel_list(self, value):
        if isinstance(value, list):
            self._apply_channel_list = list()
            for i in value:
                self._apply_channel_list.append(i)
    @property
    def crowd_desc(self):
        return self._crowd_desc

    @crowd_desc.setter
    def crowd_desc(self, value):
        self._crowd_desc = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def external_crowd_code(self):
        return self._external_crowd_code

    @external_crowd_code.setter
    def external_crowd_code(self, value):
        self._external_crowd_code = value
    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value
    @property
    def user_list(self):
        return self._user_list

    @user_list.setter
    def user_list(self, value):
        if isinstance(value, list):
            self._user_list = list()
            for i in value:
                if isinstance(i, QipanMerchantCrowdUser):
                    self._user_list.append(i)
                else:
                    self._user_list.append(QipanMerchantCrowdUser.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_channel_list:
            if isinstance(self.apply_channel_list, list):
                for i in range(0, len(self.apply_channel_list)):
                    element = self.apply_channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_channel_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_channel_list, 'to_alipay_dict'):
                params['apply_channel_list'] = self.apply_channel_list.to_alipay_dict()
            else:
                params['apply_channel_list'] = self.apply_channel_list
        if self.crowd_desc:
            if hasattr(self.crowd_desc, 'to_alipay_dict'):
                params['crowd_desc'] = self.crowd_desc.to_alipay_dict()
            else:
                params['crowd_desc'] = self.crowd_desc
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.external_crowd_code:
            if hasattr(self.external_crowd_code, 'to_alipay_dict'):
                params['external_crowd_code'] = self.external_crowd_code.to_alipay_dict()
            else:
                params['external_crowd_code'] = self.external_crowd_code
        if self.hidden:
            if hasattr(self.hidden, 'to_alipay_dict'):
                params['hidden'] = self.hidden.to_alipay_dict()
            else:
                params['hidden'] = self.hidden
        if self.user_list:
            if isinstance(self.user_list, list):
                for i in range(0, len(self.user_list)):
                    element = self.user_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_list[i] = element.to_alipay_dict()
            if hasattr(self.user_list, 'to_alipay_dict'):
                params['user_list'] = self.user_list.to_alipay_dict()
            else:
                params['user_list'] = self.user_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanCrowdCreateModel()
        if 'apply_channel_list' in d:
            o.apply_channel_list = d['apply_channel_list']
        if 'crowd_desc' in d:
            o.crowd_desc = d['crowd_desc']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'external_crowd_code' in d:
            o.external_crowd_code = d['external_crowd_code']
        if 'hidden' in d:
            o.hidden = d['hidden']
        if 'user_list' in d:
            o.user_list = d['user_list']
        return o


