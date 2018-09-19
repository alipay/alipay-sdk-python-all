#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertSpecialAdvContentRequest import KbAdvertSpecialAdvContentRequest


class KoubeiAdvertCommissionSpecialadvcontentModifyModel(object):

    def __init__(self):
        self._adv_id = None
        self._channel_id = None
        self._content_list = None
        self._modify_type = None

    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, KbAdvertSpecialAdvContentRequest):
                    self._content_list.append(i)
                else:
                    self._content_list.append(KbAdvertSpecialAdvContentRequest.from_alipay_dict(i))
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionSpecialadvcontentModifyModel()
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        return o


