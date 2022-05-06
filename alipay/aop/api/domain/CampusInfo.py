#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CampusInfo(object):

    def __init__(self):
        self._address = None
        self._campus_id = None
        self._campus_name = None
        self._inst_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CampusInfo()
        if 'address' in d:
            o.address = d['address']
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        return o


