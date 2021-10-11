#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Deliverable(object):

    def __init__(self):
        self._acceptor = None
        self._content = None
        self._remark = None
        self._standard = None

    @property
    def acceptor(self):
        return self._acceptor

    @acceptor.setter
    def acceptor(self, value):
        self._acceptor = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def standard(self):
        return self._standard

    @standard.setter
    def standard(self, value):
        self._standard = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptor:
            if hasattr(self.acceptor, 'to_alipay_dict'):
                params['acceptor'] = self.acceptor.to_alipay_dict()
            else:
                params['acceptor'] = self.acceptor
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.standard:
            if hasattr(self.standard, 'to_alipay_dict'):
                params['standard'] = self.standard.to_alipay_dict()
            else:
                params['standard'] = self.standard
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Deliverable()
        if 'acceptor' in d:
            o.acceptor = d['acceptor']
        if 'content' in d:
            o.content = d['content']
        if 'remark' in d:
            o.remark = d['remark']
        if 'standard' in d:
            o.standard = d['standard']
        return o


