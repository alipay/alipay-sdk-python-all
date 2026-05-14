#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LsItemCustomAttrItem import LsItemCustomAttrItem


class LsItemCustomAttr(object):

    def __init__(self):
        self._attrs = None
        self._group_name = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, LsItemCustomAttrItem):
                    self._attrs.append(i)
                else:
                    self._attrs.append(LsItemCustomAttrItem.from_alipay_dict(i))
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LsItemCustomAttr()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'group_name' in d:
            o.group_name = d['group_name']
        return o


