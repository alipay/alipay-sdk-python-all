#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceExtInfoMap(object):

    def __init__(self):
        self._service_pic = None

    @property
    def service_pic(self):
        return self._service_pic

    @service_pic.setter
    def service_pic(self, value):
        self._service_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_pic:
            if hasattr(self.service_pic, 'to_alipay_dict'):
                params['service_pic'] = self.service_pic.to_alipay_dict()
            else:
                params['service_pic'] = self.service_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceExtInfoMap()
        if 'service_pic' in d:
            o.service_pic = d['service_pic']
        return o


