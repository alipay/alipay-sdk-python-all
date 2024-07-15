#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmCardPictureInfo(object):

    def __init__(self):
        self._name = None
        self._out_biz_no = None
        self._picture_id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def picture_id(self):
        return self._picture_id

    @picture_id.setter
    def picture_id(self, value):
        self._picture_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.picture_id:
            if hasattr(self.picture_id, 'to_alipay_dict'):
                params['picture_id'] = self.picture_id.to_alipay_dict()
            else:
                params['picture_id'] = self.picture_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmCardPictureInfo()
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'picture_id' in d:
            o.picture_id = d['picture_id']
        return o


