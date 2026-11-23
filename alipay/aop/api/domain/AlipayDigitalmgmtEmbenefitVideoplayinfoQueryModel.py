#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtEmbenefitVideoplayinfoQueryModel(object):

    def __init__(self):
        self._attachment_id = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_id:
            if hasattr(self.attachment_id, 'to_alipay_dict'):
                params['attachment_id'] = self.attachment_id.to_alipay_dict()
            else:
                params['attachment_id'] = self.attachment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtEmbenefitVideoplayinfoQueryModel()
        if 'attachment_id' in d:
            o.attachment_id = d['attachment_id']
        return o


