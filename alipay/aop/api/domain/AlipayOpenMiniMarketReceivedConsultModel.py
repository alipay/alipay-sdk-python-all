#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniMarketReceivedConsultModel(object):

    def __init__(self):
        self._deliver_id = None
        self._deliver_id_list = None
        self._multi_deliver = None
        self._user_id = None

    @property
    def deliver_id(self):
        return self._deliver_id

    @deliver_id.setter
    def deliver_id(self, value):
        self._deliver_id = value
    @property
    def deliver_id_list(self):
        return self._deliver_id_list

    @deliver_id_list.setter
    def deliver_id_list(self, value):
        if isinstance(value, list):
            self._deliver_id_list = list()
            for i in value:
                self._deliver_id_list.append(i)
    @property
    def multi_deliver(self):
        return self._multi_deliver

    @multi_deliver.setter
    def multi_deliver(self, value):
        self._multi_deliver = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.deliver_id:
            if hasattr(self.deliver_id, 'to_alipay_dict'):
                params['deliver_id'] = self.deliver_id.to_alipay_dict()
            else:
                params['deliver_id'] = self.deliver_id
        if self.deliver_id_list:
            if isinstance(self.deliver_id_list, list):
                for i in range(0, len(self.deliver_id_list)):
                    element = self.deliver_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deliver_id_list[i] = element.to_alipay_dict()
            if hasattr(self.deliver_id_list, 'to_alipay_dict'):
                params['deliver_id_list'] = self.deliver_id_list.to_alipay_dict()
            else:
                params['deliver_id_list'] = self.deliver_id_list
        if self.multi_deliver:
            if hasattr(self.multi_deliver, 'to_alipay_dict'):
                params['multi_deliver'] = self.multi_deliver.to_alipay_dict()
            else:
                params['multi_deliver'] = self.multi_deliver
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMarketReceivedConsultModel()
        if 'deliver_id' in d:
            o.deliver_id = d['deliver_id']
        if 'deliver_id_list' in d:
            o.deliver_id_list = d['deliver_id_list']
        if 'multi_deliver' in d:
            o.multi_deliver = d['multi_deliver']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


