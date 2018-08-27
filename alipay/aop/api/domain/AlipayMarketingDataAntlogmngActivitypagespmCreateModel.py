#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingDataAntlogmngActivitypagespmCreateModel(object):

    def __init__(self):
        self._activity_id = None
        self._owner = None
        self._spma = None
        self._spmb = None
        self._title = None
        self._url = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def spma(self):
        return self._spma

    @spma.setter
    def spma(self, value):
        self._spma = value
    @property
    def spmb(self):
        return self._spmb

    @spmb.setter
    def spmb(self, value):
        self._spmb = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.spma:
            if hasattr(self.spma, 'to_alipay_dict'):
                params['spma'] = self.spma.to_alipay_dict()
            else:
                params['spma'] = self.spma
        if self.spmb:
            if hasattr(self.spmb, 'to_alipay_dict'):
                params['spmb'] = self.spmb.to_alipay_dict()
            else:
                params['spmb'] = self.spmb
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingDataAntlogmngActivitypagespmCreateModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'owner' in d:
            o.owner = d['owner']
        if 'spma' in d:
            o.spma = d['spma']
        if 'spmb' in d:
            o.spmb = d['spmb']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


