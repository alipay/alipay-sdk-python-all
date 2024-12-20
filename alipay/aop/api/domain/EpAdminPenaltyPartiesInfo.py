#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpAdminPenaltyPunishDetailsInfo import EpAdminPenaltyPunishDetailsInfo


class EpAdminPenaltyPartiesInfo(object):

    def __init__(self):
        self._name = None
        self._punish_details = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def punish_details(self):
        return self._punish_details

    @punish_details.setter
    def punish_details(self, value):
        if isinstance(value, list):
            self._punish_details = list()
            for i in value:
                if isinstance(i, EpAdminPenaltyPunishDetailsInfo):
                    self._punish_details.append(i)
                else:
                    self._punish_details.append(EpAdminPenaltyPunishDetailsInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.punish_details:
            if isinstance(self.punish_details, list):
                for i in range(0, len(self.punish_details)):
                    element = self.punish_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punish_details[i] = element.to_alipay_dict()
            if hasattr(self.punish_details, 'to_alipay_dict'):
                params['punish_details'] = self.punish_details.to_alipay_dict()
            else:
                params['punish_details'] = self.punish_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAdminPenaltyPartiesInfo()
        if 'name' in d:
            o.name = d['name']
        if 'punish_details' in d:
            o.punish_details = d['punish_details']
        return o


