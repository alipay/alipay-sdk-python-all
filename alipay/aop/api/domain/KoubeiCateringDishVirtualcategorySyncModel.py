#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishVirtualCatetorySimplifyInfo import KbdishVirtualCatetorySimplifyInfo


class KoubeiCateringDishVirtualcategorySyncModel(object):

    def __init__(self):
        self._catetory_info = None

    @property
    def catetory_info(self):
        return self._catetory_info

    @catetory_info.setter
    def catetory_info(self, value):
        if isinstance(value, KbdishVirtualCatetorySimplifyInfo):
            self._catetory_info = value
        else:
            self._catetory_info = KbdishVirtualCatetorySimplifyInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_info:
            if hasattr(self.catetory_info, 'to_alipay_dict'):
                params['catetory_info'] = self.catetory_info.to_alipay_dict()
            else:
                params['catetory_info'] = self.catetory_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishVirtualcategorySyncModel()
        if 'catetory_info' in d:
            o.catetory_info = d['catetory_info']
        return o


