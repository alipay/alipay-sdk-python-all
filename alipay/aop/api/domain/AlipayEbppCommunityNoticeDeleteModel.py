#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityNoticeDeleteModel(object):

    def __init__(self):
        self._alipay_notice_id = None
        self._biz_type = None
        self._sub_biz_type = None

    @property
    def alipay_notice_id(self):
        return self._alipay_notice_id

    @alipay_notice_id.setter
    def alipay_notice_id(self, value):
        self._alipay_notice_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_notice_id:
            if hasattr(self.alipay_notice_id, 'to_alipay_dict'):
                params['alipay_notice_id'] = self.alipay_notice_id.to_alipay_dict()
            else:
                params['alipay_notice_id'] = self.alipay_notice_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityNoticeDeleteModel()
        if 'alipay_notice_id' in d:
            o.alipay_notice_id = d['alipay_notice_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


