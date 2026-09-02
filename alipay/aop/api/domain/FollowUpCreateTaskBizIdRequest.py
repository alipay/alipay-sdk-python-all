#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FollowUpCreateTaskBizIdRequest(object):

    def __init__(self):
        self._aq_open_id = None
        self._biz_id = None

    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_open_id:
            if hasattr(self.aq_open_id, 'to_alipay_dict'):
                params['aq_open_id'] = self.aq_open_id.to_alipay_dict()
            else:
                params['aq_open_id'] = self.aq_open_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FollowUpCreateTaskBizIdRequest()
        if 'aq_open_id' in d:
            o.aq_open_id = d['aq_open_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        return o


