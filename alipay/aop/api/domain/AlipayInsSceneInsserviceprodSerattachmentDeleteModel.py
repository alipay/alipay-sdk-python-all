#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInsserviceprodSerattachmentDeleteModel(object):

    def __init__(self):
        self._attachment_no = None

    @property
    def attachment_no(self):
        return self._attachment_no

    @attachment_no.setter
    def attachment_no(self, value):
        self._attachment_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_no:
            if hasattr(self.attachment_no, 'to_alipay_dict'):
                params['attachment_no'] = self.attachment_no.to_alipay_dict()
            else:
                params['attachment_no'] = self.attachment_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsserviceprodSerattachmentDeleteModel()
        if 'attachment_no' in d:
            o.attachment_no = d['attachment_no']
        return o


