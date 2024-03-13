#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PopulationDTO import PopulationDTO
from alipay.aop.api.domain.PopulationDTO import PopulationDTO
from alipay.aop.api.domain.PopulationDTO import PopulationDTO


class PortraitInMallResDTO(object):

    def __init__(self):
        self._live_user = None
        self._settled_user = None
        self._work_user = None

    @property
    def live_user(self):
        return self._live_user

    @live_user.setter
    def live_user(self, value):
        if isinstance(value, PopulationDTO):
            self._live_user = value
        else:
            self._live_user = PopulationDTO.from_alipay_dict(value)
    @property
    def settled_user(self):
        return self._settled_user

    @settled_user.setter
    def settled_user(self, value):
        if isinstance(value, PopulationDTO):
            self._settled_user = value
        else:
            self._settled_user = PopulationDTO.from_alipay_dict(value)
    @property
    def work_user(self):
        return self._work_user

    @work_user.setter
    def work_user(self, value):
        if isinstance(value, PopulationDTO):
            self._work_user = value
        else:
            self._work_user = PopulationDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.live_user:
            if hasattr(self.live_user, 'to_alipay_dict'):
                params['live_user'] = self.live_user.to_alipay_dict()
            else:
                params['live_user'] = self.live_user
        if self.settled_user:
            if hasattr(self.settled_user, 'to_alipay_dict'):
                params['settled_user'] = self.settled_user.to_alipay_dict()
            else:
                params['settled_user'] = self.settled_user
        if self.work_user:
            if hasattr(self.work_user, 'to_alipay_dict'):
                params['work_user'] = self.work_user.to_alipay_dict()
            else:
                params['work_user'] = self.work_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortraitInMallResDTO()
        if 'live_user' in d:
            o.live_user = d['live_user']
        if 'settled_user' in d:
            o.settled_user = d['settled_user']
        if 'work_user' in d:
            o.work_user = d['work_user']
        return o


