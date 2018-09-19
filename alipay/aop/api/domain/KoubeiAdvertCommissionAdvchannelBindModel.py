#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionAdvchannelBindModel(object):

    def __init__(self):
        self._adv_id = None
        self._channel_id_list = None

    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def channel_id_list(self):
        return self._channel_id_list

    @channel_id_list.setter
    def channel_id_list(self, value):
        if isinstance(value, list):
            self._channel_id_list = list()
            for i in value:
                self._channel_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.channel_id_list:
            if isinstance(self.channel_id_list, list):
                for i in range(0, len(self.channel_id_list)):
                    element = self.channel_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_id_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_id_list, 'to_alipay_dict'):
                params['channel_id_list'] = self.channel_id_list.to_alipay_dict()
            else:
                params['channel_id_list'] = self.channel_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionAdvchannelBindModel()
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'channel_id_list' in d:
            o.channel_id_list = d['channel_id_list']
        return o


