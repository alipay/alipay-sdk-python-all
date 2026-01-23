#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySupervisionTransfermaterialSubmitModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._biz_scene = None
        self._confirm_period = None
        self._file_ids = None
        self._open_id = None
        self._out_flow_id = None
        self._out_order_no = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def confirm_period(self):
        return self._confirm_period

    @confirm_period.setter
    def confirm_period(self, value):
        self._confirm_period = value
    @property
    def file_ids(self):
        return self._file_ids

    @file_ids.setter
    def file_ids(self, value):
        if isinstance(value, list):
            self._file_ids = list()
            for i in value:
                self._file_ids.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_flow_id(self):
        return self._out_flow_id

    @out_flow_id.setter
    def out_flow_id(self, value):
        self._out_flow_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.confirm_period:
            if hasattr(self.confirm_period, 'to_alipay_dict'):
                params['confirm_period'] = self.confirm_period.to_alipay_dict()
            else:
                params['confirm_period'] = self.confirm_period
        if self.file_ids:
            if isinstance(self.file_ids, list):
                for i in range(0, len(self.file_ids)):
                    element = self.file_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_ids[i] = element.to_alipay_dict()
            if hasattr(self.file_ids, 'to_alipay_dict'):
                params['file_ids'] = self.file_ids.to_alipay_dict()
            else:
                params['file_ids'] = self.file_ids
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_flow_id:
            if hasattr(self.out_flow_id, 'to_alipay_dict'):
                params['out_flow_id'] = self.out_flow_id.to_alipay_dict()
            else:
                params['out_flow_id'] = self.out_flow_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySupervisionTransfermaterialSubmitModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'confirm_period' in d:
            o.confirm_period = d['confirm_period']
        if 'file_ids' in d:
            o.file_ids = d['file_ids']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_flow_id' in d:
            o.out_flow_id = d['out_flow_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


