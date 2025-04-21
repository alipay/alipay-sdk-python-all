#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftPoapDistributeSubmitModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_time = None
        self._id_no = None
        self._id_type = None
        self._medal_meta_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def medal_meta_id(self):
        return self._medal_meta_id

    @medal_meta_id.setter
    def medal_meta_id(self, value):
        self._medal_meta_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.medal_meta_id:
            if hasattr(self.medal_meta_id, 'to_alipay_dict'):
                params['medal_meta_id'] = self.medal_meta_id.to_alipay_dict()
            else:
                params['medal_meta_id'] = self.medal_meta_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftPoapDistributeSubmitModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'medal_meta_id' in d:
            o.medal_meta_id = d['medal_meta_id']
        return o


