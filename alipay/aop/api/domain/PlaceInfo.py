#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlaceInfo(object):

    def __init__(self):
        self._inst_id = None
        self._out_biz_no = None
        self._parent_out_biz_no = None
        self._parent_place_id = None
        self._parent_place_name = None
        self._place_id = None
        self._place_name = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def parent_out_biz_no(self):
        return self._parent_out_biz_no

    @parent_out_biz_no.setter
    def parent_out_biz_no(self, value):
        self._parent_out_biz_no = value
    @property
    def parent_place_id(self):
        return self._parent_place_id

    @parent_place_id.setter
    def parent_place_id(self, value):
        self._parent_place_id = value
    @property
    def parent_place_name(self):
        return self._parent_place_name

    @parent_place_name.setter
    def parent_place_name(self, value):
        self._parent_place_name = value
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.parent_out_biz_no:
            if hasattr(self.parent_out_biz_no, 'to_alipay_dict'):
                params['parent_out_biz_no'] = self.parent_out_biz_no.to_alipay_dict()
            else:
                params['parent_out_biz_no'] = self.parent_out_biz_no
        if self.parent_place_id:
            if hasattr(self.parent_place_id, 'to_alipay_dict'):
                params['parent_place_id'] = self.parent_place_id.to_alipay_dict()
            else:
                params['parent_place_id'] = self.parent_place_id
        if self.parent_place_name:
            if hasattr(self.parent_place_name, 'to_alipay_dict'):
                params['parent_place_name'] = self.parent_place_name.to_alipay_dict()
            else:
                params['parent_place_name'] = self.parent_place_name
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlaceInfo()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'parent_out_biz_no' in d:
            o.parent_out_biz_no = d['parent_out_biz_no']
        if 'parent_place_id' in d:
            o.parent_place_id = d['parent_place_id']
        if 'parent_place_name' in d:
            o.parent_place_name = d['parent_place_name']
        if 'place_id' in d:
            o.place_id = d['place_id']
        if 'place_name' in d:
            o.place_name = d['place_name']
        return o


