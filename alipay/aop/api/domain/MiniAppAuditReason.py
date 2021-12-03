#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppAuditReasonMemo import MiniAppAuditReasonMemo


class MiniAppAuditReason(object):

    def __init__(self):
        self._audit_images = None
        self._memos = None

    @property
    def audit_images(self):
        return self._audit_images

    @audit_images.setter
    def audit_images(self, value):
        if isinstance(value, list):
            self._audit_images = list()
            for i in value:
                self._audit_images.append(i)
    @property
    def memos(self):
        return self._memos

    @memos.setter
    def memos(self, value):
        if isinstance(value, list):
            self._memos = list()
            for i in value:
                if isinstance(i, MiniAppAuditReasonMemo):
                    self._memos.append(i)
                else:
                    self._memos.append(MiniAppAuditReasonMemo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.audit_images:
            if isinstance(self.audit_images, list):
                for i in range(0, len(self.audit_images)):
                    element = self.audit_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audit_images[i] = element.to_alipay_dict()
            if hasattr(self.audit_images, 'to_alipay_dict'):
                params['audit_images'] = self.audit_images.to_alipay_dict()
            else:
                params['audit_images'] = self.audit_images
        if self.memos:
            if isinstance(self.memos, list):
                for i in range(0, len(self.memos)):
                    element = self.memos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.memos[i] = element.to_alipay_dict()
            if hasattr(self.memos, 'to_alipay_dict'):
                params['memos'] = self.memos.to_alipay_dict()
            else:
                params['memos'] = self.memos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppAuditReason()
        if 'audit_images' in d:
            o.audit_images = d['audit_images']
        if 'memos' in d:
            o.memos = d['memos']
        return o


