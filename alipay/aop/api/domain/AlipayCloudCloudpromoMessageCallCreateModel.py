#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactStrategy import ContactStrategy
from alipay.aop.api.domain.CallUserInfo import CallUserInfo


class AlipayCloudCloudpromoMessageCallCreateModel(object):

    def __init__(self):
        self._contact_strategy = None
        self._contact_type = None
        self._user_infos = None

    @property
    def contact_strategy(self):
        return self._contact_strategy

    @contact_strategy.setter
    def contact_strategy(self, value):
        if isinstance(value, ContactStrategy):
            self._contact_strategy = value
        else:
            self._contact_strategy = ContactStrategy.from_alipay_dict(value)
    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value
    @property
    def user_infos(self):
        return self._user_infos

    @user_infos.setter
    def user_infos(self, value):
        if isinstance(value, list):
            self._user_infos = list()
            for i in value:
                if isinstance(i, CallUserInfo):
                    self._user_infos.append(i)
                else:
                    self._user_infos.append(CallUserInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.contact_strategy:
            if hasattr(self.contact_strategy, 'to_alipay_dict'):
                params['contact_strategy'] = self.contact_strategy.to_alipay_dict()
            else:
                params['contact_strategy'] = self.contact_strategy
        if self.contact_type:
            if hasattr(self.contact_type, 'to_alipay_dict'):
                params['contact_type'] = self.contact_type.to_alipay_dict()
            else:
                params['contact_type'] = self.contact_type
        if self.user_infos:
            if isinstance(self.user_infos, list):
                for i in range(0, len(self.user_infos)):
                    element = self.user_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_infos[i] = element.to_alipay_dict()
            if hasattr(self.user_infos, 'to_alipay_dict'):
                params['user_infos'] = self.user_infos.to_alipay_dict()
            else:
                params['user_infos'] = self.user_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMessageCallCreateModel()
        if 'contact_strategy' in d:
            o.contact_strategy = d['contact_strategy']
        if 'contact_type' in d:
            o.contact_type = d['contact_type']
        if 'user_infos' in d:
            o.user_infos = d['user_infos']
        return o


