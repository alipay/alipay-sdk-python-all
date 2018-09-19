#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelContentCancelModel(object):

    def __init__(self):
        self._content_id = None
        self._modified_date = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def modified_date(self):
        return self._modified_date

    @modified_date.setter
    def modified_date(self, value):
        self._modified_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.modified_date:
            if hasattr(self.modified_date, 'to_alipay_dict'):
                params['modified_date'] = self.modified_date.to_alipay_dict()
            else:
                params['modified_date'] = self.modified_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelContentCancelModel()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'modified_date' in d:
            o.modified_date = d['modified_date']
        return o


