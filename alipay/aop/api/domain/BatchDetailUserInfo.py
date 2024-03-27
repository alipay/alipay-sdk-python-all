#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BatchDetailUserInfo(object):

    def __init__(self):
        self._trans_in_entity_biz_type = None
        self._trans_in_entity_id = None
        self._trans_in_entity_id_type = None
        self._trans_out_entity_biz_type = None
        self._trans_out_entity_id = None
        self._trans_out_entity_id_type = None

    @property
    def trans_in_entity_biz_type(self):
        return self._trans_in_entity_biz_type

    @trans_in_entity_biz_type.setter
    def trans_in_entity_biz_type(self, value):
        self._trans_in_entity_biz_type = value
    @property
    def trans_in_entity_id(self):
        return self._trans_in_entity_id

    @trans_in_entity_id.setter
    def trans_in_entity_id(self, value):
        self._trans_in_entity_id = value
    @property
    def trans_in_entity_id_type(self):
        return self._trans_in_entity_id_type

    @trans_in_entity_id_type.setter
    def trans_in_entity_id_type(self, value):
        self._trans_in_entity_id_type = value
    @property
    def trans_out_entity_biz_type(self):
        return self._trans_out_entity_biz_type

    @trans_out_entity_biz_type.setter
    def trans_out_entity_biz_type(self, value):
        self._trans_out_entity_biz_type = value
    @property
    def trans_out_entity_id(self):
        return self._trans_out_entity_id

    @trans_out_entity_id.setter
    def trans_out_entity_id(self, value):
        self._trans_out_entity_id = value
    @property
    def trans_out_entity_id_type(self):
        return self._trans_out_entity_id_type

    @trans_out_entity_id_type.setter
    def trans_out_entity_id_type(self, value):
        self._trans_out_entity_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.trans_in_entity_biz_type:
            if hasattr(self.trans_in_entity_biz_type, 'to_alipay_dict'):
                params['trans_in_entity_biz_type'] = self.trans_in_entity_biz_type.to_alipay_dict()
            else:
                params['trans_in_entity_biz_type'] = self.trans_in_entity_biz_type
        if self.trans_in_entity_id:
            if hasattr(self.trans_in_entity_id, 'to_alipay_dict'):
                params['trans_in_entity_id'] = self.trans_in_entity_id.to_alipay_dict()
            else:
                params['trans_in_entity_id'] = self.trans_in_entity_id
        if self.trans_in_entity_id_type:
            if hasattr(self.trans_in_entity_id_type, 'to_alipay_dict'):
                params['trans_in_entity_id_type'] = self.trans_in_entity_id_type.to_alipay_dict()
            else:
                params['trans_in_entity_id_type'] = self.trans_in_entity_id_type
        if self.trans_out_entity_biz_type:
            if hasattr(self.trans_out_entity_biz_type, 'to_alipay_dict'):
                params['trans_out_entity_biz_type'] = self.trans_out_entity_biz_type.to_alipay_dict()
            else:
                params['trans_out_entity_biz_type'] = self.trans_out_entity_biz_type
        if self.trans_out_entity_id:
            if hasattr(self.trans_out_entity_id, 'to_alipay_dict'):
                params['trans_out_entity_id'] = self.trans_out_entity_id.to_alipay_dict()
            else:
                params['trans_out_entity_id'] = self.trans_out_entity_id
        if self.trans_out_entity_id_type:
            if hasattr(self.trans_out_entity_id_type, 'to_alipay_dict'):
                params['trans_out_entity_id_type'] = self.trans_out_entity_id_type.to_alipay_dict()
            else:
                params['trans_out_entity_id_type'] = self.trans_out_entity_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BatchDetailUserInfo()
        if 'trans_in_entity_biz_type' in d:
            o.trans_in_entity_biz_type = d['trans_in_entity_biz_type']
        if 'trans_in_entity_id' in d:
            o.trans_in_entity_id = d['trans_in_entity_id']
        if 'trans_in_entity_id_type' in d:
            o.trans_in_entity_id_type = d['trans_in_entity_id_type']
        if 'trans_out_entity_biz_type' in d:
            o.trans_out_entity_biz_type = d['trans_out_entity_biz_type']
        if 'trans_out_entity_id' in d:
            o.trans_out_entity_id = d['trans_out_entity_id']
        if 'trans_out_entity_id_type' in d:
            o.trans_out_entity_id_type = d['trans_out_entity_id_type']
        return o


