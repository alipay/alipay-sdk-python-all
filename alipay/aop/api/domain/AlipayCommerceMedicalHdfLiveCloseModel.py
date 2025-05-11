#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfLiveCloseModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._live_prepare_type = None
        self._out_doc_id = None
        self._out_live_id = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def live_prepare_type(self):
        return self._live_prepare_type

    @live_prepare_type.setter
    def live_prepare_type(self, value):
        self._live_prepare_type = value
    @property
    def out_doc_id(self):
        return self._out_doc_id

    @out_doc_id.setter
    def out_doc_id(self, value):
        self._out_doc_id = value
    @property
    def out_live_id(self):
        return self._out_live_id

    @out_live_id.setter
    def out_live_id(self, value):
        self._out_live_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.live_prepare_type:
            if hasattr(self.live_prepare_type, 'to_alipay_dict'):
                params['live_prepare_type'] = self.live_prepare_type.to_alipay_dict()
            else:
                params['live_prepare_type'] = self.live_prepare_type
        if self.out_doc_id:
            if hasattr(self.out_doc_id, 'to_alipay_dict'):
                params['out_doc_id'] = self.out_doc_id.to_alipay_dict()
            else:
                params['out_doc_id'] = self.out_doc_id
        if self.out_live_id:
            if hasattr(self.out_live_id, 'to_alipay_dict'):
                params['out_live_id'] = self.out_live_id.to_alipay_dict()
            else:
                params['out_live_id'] = self.out_live_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfLiveCloseModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'live_prepare_type' in d:
            o.live_prepare_type = d['live_prepare_type']
        if 'out_doc_id' in d:
            o.out_doc_id = d['out_doc_id']
        if 'out_live_id' in d:
            o.out_live_id = d['out_live_id']
        return o


