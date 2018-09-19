#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductVOOptions(object):

    def __init__(self):
        self._include_condition_group = None
        self._include_prod_base = None
        self._include_prod_ip = None
        self._include_prod_lo = None
        self._include_prod_mark = None
        self._include_prod_rel = None
        self._include_prod_ri = None

    @property
    def include_condition_group(self):
        return self._include_condition_group

    @include_condition_group.setter
    def include_condition_group(self, value):
        self._include_condition_group = value
    @property
    def include_prod_base(self):
        return self._include_prod_base

    @include_prod_base.setter
    def include_prod_base(self, value):
        self._include_prod_base = value
    @property
    def include_prod_ip(self):
        return self._include_prod_ip

    @include_prod_ip.setter
    def include_prod_ip(self, value):
        self._include_prod_ip = value
    @property
    def include_prod_lo(self):
        return self._include_prod_lo

    @include_prod_lo.setter
    def include_prod_lo(self, value):
        self._include_prod_lo = value
    @property
    def include_prod_mark(self):
        return self._include_prod_mark

    @include_prod_mark.setter
    def include_prod_mark(self, value):
        self._include_prod_mark = value
    @property
    def include_prod_rel(self):
        return self._include_prod_rel

    @include_prod_rel.setter
    def include_prod_rel(self, value):
        self._include_prod_rel = value
    @property
    def include_prod_ri(self):
        return self._include_prod_ri

    @include_prod_ri.setter
    def include_prod_ri(self, value):
        self._include_prod_ri = value


    def to_alipay_dict(self):
        params = dict()
        if self.include_condition_group:
            if hasattr(self.include_condition_group, 'to_alipay_dict'):
                params['include_condition_group'] = self.include_condition_group.to_alipay_dict()
            else:
                params['include_condition_group'] = self.include_condition_group
        if self.include_prod_base:
            if hasattr(self.include_prod_base, 'to_alipay_dict'):
                params['include_prod_base'] = self.include_prod_base.to_alipay_dict()
            else:
                params['include_prod_base'] = self.include_prod_base
        if self.include_prod_ip:
            if hasattr(self.include_prod_ip, 'to_alipay_dict'):
                params['include_prod_ip'] = self.include_prod_ip.to_alipay_dict()
            else:
                params['include_prod_ip'] = self.include_prod_ip
        if self.include_prod_lo:
            if hasattr(self.include_prod_lo, 'to_alipay_dict'):
                params['include_prod_lo'] = self.include_prod_lo.to_alipay_dict()
            else:
                params['include_prod_lo'] = self.include_prod_lo
        if self.include_prod_mark:
            if hasattr(self.include_prod_mark, 'to_alipay_dict'):
                params['include_prod_mark'] = self.include_prod_mark.to_alipay_dict()
            else:
                params['include_prod_mark'] = self.include_prod_mark
        if self.include_prod_rel:
            if hasattr(self.include_prod_rel, 'to_alipay_dict'):
                params['include_prod_rel'] = self.include_prod_rel.to_alipay_dict()
            else:
                params['include_prod_rel'] = self.include_prod_rel
        if self.include_prod_ri:
            if hasattr(self.include_prod_ri, 'to_alipay_dict'):
                params['include_prod_ri'] = self.include_prod_ri.to_alipay_dict()
            else:
                params['include_prod_ri'] = self.include_prod_ri
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductVOOptions()
        if 'include_condition_group' in d:
            o.include_condition_group = d['include_condition_group']
        if 'include_prod_base' in d:
            o.include_prod_base = d['include_prod_base']
        if 'include_prod_ip' in d:
            o.include_prod_ip = d['include_prod_ip']
        if 'include_prod_lo' in d:
            o.include_prod_lo = d['include_prod_lo']
        if 'include_prod_mark' in d:
            o.include_prod_mark = d['include_prod_mark']
        if 'include_prod_rel' in d:
            o.include_prod_rel = d['include_prod_rel']
        if 'include_prod_ri' in d:
            o.include_prod_ri = d['include_prod_ri']
        return o


