#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOrderChangedExtendInfoVO(object):

    def __init__(self):
        self._rent_dispatch_id = None

    @property
    def rent_dispatch_id(self):
        return self._rent_dispatch_id

    @rent_dispatch_id.setter
    def rent_dispatch_id(self, value):
        self._rent_dispatch_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.rent_dispatch_id:
            if hasattr(self.rent_dispatch_id, 'to_alipay_dict'):
                params['rent_dispatch_id'] = self.rent_dispatch_id.to_alipay_dict()
            else:
                params['rent_dispatch_id'] = self.rent_dispatch_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderChangedExtendInfoVO()
        if 'rent_dispatch_id' in d:
            o.rent_dispatch_id = d['rent_dispatch_id']
        return o


