#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HSchoolInfo import HSchoolInfo


class UserIdentityInfo(object):

    def __init__(self):
        self._h_school_info = None

    @property
    def h_school_info(self):
        return self._h_school_info

    @h_school_info.setter
    def h_school_info(self, value):
        if isinstance(value, HSchoolInfo):
            self._h_school_info = value
        else:
            self._h_school_info = HSchoolInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.h_school_info:
            if hasattr(self.h_school_info, 'to_alipay_dict'):
                params['h_school_info'] = self.h_school_info.to_alipay_dict()
            else:
                params['h_school_info'] = self.h_school_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserIdentityInfo()
        if 'h_school_info' in d:
            o.h_school_info = d['h_school_info']
        return o


