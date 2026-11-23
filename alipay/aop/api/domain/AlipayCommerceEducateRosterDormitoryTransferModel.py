#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateRosterDormitoryTransferModel(object):

    def __init__(self):
        self._employee_no = None
        self._inst_id = None
        self._open_id = None
        self._place_out_biz_no = None
        self._pre_place_out_biz_no = None
        self._uid = None

    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def place_out_biz_no(self):
        return self._place_out_biz_no

    @place_out_biz_no.setter
    def place_out_biz_no(self, value):
        self._place_out_biz_no = value
    @property
    def pre_place_out_biz_no(self):
        return self._pre_place_out_biz_no

    @pre_place_out_biz_no.setter
    def pre_place_out_biz_no(self, value):
        self._pre_place_out_biz_no = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.place_out_biz_no:
            if hasattr(self.place_out_biz_no, 'to_alipay_dict'):
                params['place_out_biz_no'] = self.place_out_biz_no.to_alipay_dict()
            else:
                params['place_out_biz_no'] = self.place_out_biz_no
        if self.pre_place_out_biz_no:
            if hasattr(self.pre_place_out_biz_no, 'to_alipay_dict'):
                params['pre_place_out_biz_no'] = self.pre_place_out_biz_no.to_alipay_dict()
            else:
                params['pre_place_out_biz_no'] = self.pre_place_out_biz_no
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateRosterDormitoryTransferModel()
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'place_out_biz_no' in d:
            o.place_out_biz_no = d['place_out_biz_no']
        if 'pre_place_out_biz_no' in d:
            o.pre_place_out_biz_no = d['pre_place_out_biz_no']
        if 'uid' in d:
            o.uid = d['uid']
        return o


